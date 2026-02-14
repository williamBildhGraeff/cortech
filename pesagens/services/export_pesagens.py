from animais.models import Animal
from django.core.exceptions import ObjectDoesNotExist
class ExportarCsvPesagemService:
    @staticmethod
    def exportar_pesagens_lote_csv(lote_id):
        animais = (
            Animal.objects
            .filter(lote_id=lote_id)
            .prefetch_related('pesagens')
        )

        if not animais.exists():
            raise ObjectDoesNotExist("Lote não encontrado ou está vazio.")

        max_pesagens = max(
            (animal.pesagens.count() for animal in animais),
            default=0
        )

        dados = []

        for animal in animais:
            pesagens = animal.pesagens.all().order_by('data')

            linha = {
                'brinco': animal.brinco,
                'pesagens': [],
                'gmd_medio': None
            }

            gmds = []

            for p in pesagens:
                linha['pesagens'].append({
                    'data': str(p.data),
                    'peso': str(p.peso),
                    'classificacao': str(p.classificacao),
                    'gmd_calculado_automatico': (
                        str(p.gmd_calculado_automatico)
                        if p.gmd_calculado_automatico else ""
                    )
                })

                if p.gmd_calculado_automatico:
                    gmds.append(float(p.gmd_calculado_automatico))

            linha['gmd_medio'] = sum(gmds) / len(gmds) if gmds else None
            dados.append(linha)

        return {
            'max_pesagens': max_pesagens,
            'dados': dados
        }