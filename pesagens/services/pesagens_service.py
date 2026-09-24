
from decimal import Decimal

from django.shortcuts import get_object_or_404

from pesagens.interfaces.pesagens_interface import PesagemInterface
from pesagens.models import Pesagem
from statistics import mean, median, pstdev


def calculo_gmd(pesagem:dict):
    animal = pesagem.get('animal')
    data = pesagem.get('data')
    peso = pesagem.get('peso')
    ultima_pesagem = Pesagem.objects.filter(
        animal=animal,
        data__lt=data).order_by('-data').first()
    if not ultima_pesagem: return None
    dias = (data - ultima_pesagem.data).days
    if dias > 0:
        ganho = float(peso) - float(ultima_pesagem.peso)
        gmd_calculado_automatico = ganho / dias
        return gmd_calculado_automatico
    return None


def _recalcular_gmd_animal(animal_id: int):

    pesagens = Pesagem.objects.filter(
        animal_id=animal_id
    ).order_by('data', 'id')

    anterior = None

    for pesagem in pesagens:

        if anterior is None:
            pesagem.gmd_calculado_automatico = None

        else:
            dias = (
                    pesagem.data - anterior.data
            ).days

            if dias > 0:
                ganho = pesagem.peso - anterior.peso

                pesagem.gmd_calculado_automatico = (
                        ganho / Decimal(dias)
                )
            else:
                pesagem.gmd_calculado_automatico = None

        pesagem.save(
            update_fields=[
                'gmd_calculado_automatico'
            ]
        )

        anterior = pesagem


class PesagemService(PesagemInterface):
    def post(self, pesagem:dict, animal_id: int = None):
        gmd_calculado = calculo_gmd(pesagem)
        pesagem['gmd_calculado_automatico'] = gmd_calculado
        pesagem = Pesagem.objects.create(**pesagem)
        return pesagem

    def get(self, animal_id:int | None = None, lote_id:int | None = None):
        if animal_id:
            pesagens = Pesagem.objects.filter(animal_id=animal_id).order_by('-data', '-id')
            return self._adicionar_indicadores(pesagens)

        if lote_id:
            pesagens = Pesagem.objects.filter(animal__lote_id=lote_id).order_by('-animal__brinco', '-data')
            analise = self.analisar_lote(pesagens)
            return {
                'pesagens': pesagens,
                'analise': analise
            }


    def put(self, pesagem_id: int, dados: dict):
        pesagem = get_object_or_404(
            Pesagem,
            id=pesagem_id
        )
        for campo, valor in dados.items():
            setattr(pesagem, campo, valor)
        pesagem.save()

        _recalcular_gmd_animal(pesagem.animal_id)

        return pesagem

    def delete(self, pesagem_id: int):
        pesagem = get_object_or_404(
            Pesagem,
            id=pesagem_id
        )
        animal_id = pesagem.animal_id
        pesagem.delete()
        _recalcular_gmd_animal(animal_id)

    def _adicionar_indicadores(self, pesagens: dict):
        pesagens = list(pesagens)
        if not pesagens:
            return {
                'indicadores': {
                    'primeira_pesagem': None,
                    'ultima_pesagem': None,
                    'ganho_total': None,
                    'gmd_medio': None,
                    'gmd_atual': None,
                },
                'pesagens': []
            }
        primeira_pesagem = pesagens[-1]
        ultima_pesagem = pesagens[0]
        peso_inicial = primeira_pesagem.peso
        peso_atual = ultima_pesagem.peso
        ganho_total = peso_atual - peso_inicial
        dias = (ultima_pesagem.data - primeira_pesagem.data).days
        gmd_medio = None
        if dias > 0:
            gmd_medio = ganho_total / Decimal(dias)
        gmd_atual = ultima_pesagem.gmd_calculado_automatico
        return {
            'indicadores': {
                'primeira_pesagem': peso_inicial,
                'ultima_pesagem': peso_atual,
                'ganho_total': ganho_total,
                'gmd_medio': gmd_medio,
                'gmd_atual': gmd_atual
            },
            'pesagens': pesagens
        }

    def analisar_lote(self, pesagens: list):
        animais = {}
        for pesagem in pesagens:
            animais.setdefault(pesagem.animal_id, []).append(pesagem)
        animais_gmd = []
        for animal_id, pesagens_animal in animais.items():
            pesagens_animal.sort(
                key=lambda pesagem: (pesagem.data, pesagem.id),
                reverse = True
            )
            dados = self._adicionar_indicadores(pesagens_animal)
            gmd = dados['indicadores']['gmd_medio']
            if gmd is not None:
                animais_gmd.append({
                    'animal_id': animal_id,
                    'brinco': pesagens_animal[0].animal.brinco,
                    'gmd': gmd
                })

        gmds = [
            float(animal['gmd']) for animal in animais_gmd
        ]

        if not gmds:
            return {
                'gmd_medio': None,
                'estatisticas': None,
                'animais_gmd': None,
            }
        q1 = self._percentil(gmds, 0.25)
        q3 = self._percentil(gmds, 0.75)
        iqr = q3 - q1

        limite_inferior = q1 - (1.5 * iqr)
        limite_superior = q3 + (1.5 * iqr)
        estatisticas = {
            'media': round(mean(gmds), 2),
            'mediana': round(median(gmds), 2),
            'desvio_padrao': round(pstdev(gmds), 2),
            'q1': round(q1, 2),
            'q3': round(q3, 2),
            'iqr': round(iqr, 2),
            'limite_inferior': round(limite_inferior, 2),
            'limite_superior': round(limite_superior, 2),
            'minimo': round(min(gmds), 2),
            'maximo': round(max(gmds), 2),
        }

        outliers = []
        for animal in animais_gmd:
            if animal['gmd'] < limite_inferior:
                outliers.append({
                    'animal_id': animal['animal_id'],
                    'brinco': animal['brinco'],
                    'gmd': round(animal['gmd'], 2),
                    'tipo': 'baixo'
                })
            elif animal['gmd'] > limite_superior:
                outliers.append({
                    'animal_id': animal['animal_id'],
                    'brinco': animal['brinco'],
                    'gmd': round(animal['gmd'], 2),
                    'tipo': 'alto'
                })

        return {
            'gmd_medio': round(mean(gmds), 2),
            'estatisticas': estatisticas,
            'outliers': outliers,
            'animais_gmd': animais_gmd
        }

    def _percentil(self, valores, percentual):
        valores = sorted(valores)
        posicao = (len(valores) -1) * percentual
        inferior = int(posicao)
        superior = inferior + 1
        if superior >= len(valores):
            return valores[inferior]
        peso = posicao - inferior
        return (
            valores[inferior]
            + (valores[superior] - valores[inferior]) * peso
        )



