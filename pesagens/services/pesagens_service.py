from django.shortcuts import get_object_or_404

from pesagens.interfaces.pesagens_interface import PesagemInterface
from pesagens.models import Pesagem


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
        ganho = float(ultima_pesagem.peso) - float(peso)
        gmd_calculado_automatico = ganho / dias
        return gmd_calculado_automatico
    return None

class PesagemService(PesagemInterface):
    def post(self, pesagem:dict):
        gmd_calculado = calculo_gmd(pesagem)
        pesagem['gmd_calculado_automatico'] = gmd_calculado
        pesagem = Pesagem.objects.create(**pesagem)
        return pesagem

    def get(self, pesagem_id:int | None = None):
        if pesagem_id:
            return get_object_or_404(Pesagem, id=pesagem_id)
        return Pesagem.objects.all()



