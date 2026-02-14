class ManejoService:

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
