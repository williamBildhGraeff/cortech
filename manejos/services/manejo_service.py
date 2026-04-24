from abc import ABC

from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from animais.models import HistoricoLoteAnimal
from manejos.interfaces.manejo_interface import ManejoInterface
from manejos.models import Manejo


class ManejoService(ManejoInterface):

    def post(self, data: dict):
        animais = data.pop('animais', [])  # remove do dict
        manejo = Manejo.objects.create(**data)
        if animais:
            manejo.animais.set(animais)
        return manejo

    def get(self, manejoid:int | None = None):
        if manejoid:
            return get_object_or_404(Manejo, id=manejoid)
        return Manejo.objects.all()

    @staticmethod
    @transaction.atomic
    def criar_manejo(dados):
        tipo = dados['tipo']
        animais = dados['animais']
        lote_destino = dados.get('lote_destino')
        data = dados['data']
        observacao = dados.get('observacao')

        if tipo.move_lote and not lote_destino:
            raise ValidationError("Manejo de transferência exige lote_destino.")

        # 🔒 valida lotes de origem ANTES
        if tipo.move_lote:
            lotes_origem = {
                animal.lote_id
                for animal in animais
                if animal.lote_id is not None
            }

            if len(lotes_origem) > 1:
                raise ValidationError(
                    "Animais de lotes diferentes não podem ser transferidos no mesmo manejo."
                )
        # 1️⃣ cria o manejo
        manejo = Manejo.objects.create(
            tipo=tipo,
            data=data,
            observacao=observacao,
            lote_destino=lote_destino
        )

        # 2️⃣ vincula os animais
        manejo.animais.set(animais)

        # 3️⃣ movimentação + histórico
        if not tipo.move_lote:
            return manejo

    
        for animal in animais:

            # já está no lote destino → ignora
            if animal.lote_id == lote_destino.id:
                continue

            # histórico SEMPRE baseado no estado real
            HistoricoLoteAnimal.objects.create(
                animal=animal,
                manejo=manejo,
                lote_origem=animal.lote,
                lote_destino=lote_destino,
                data=manejo.data,
                origem="manual"
            )

            # atualiza animal
            animal.lote = lote_destino
            animal.save(update_fields=['lote'])

        return manejo

