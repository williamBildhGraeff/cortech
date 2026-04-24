from rest_framework.exceptions import ValidationError


class ManejoValidators:
    @staticmethod
    def validar_manejo(manejo):
        tipo = manejo.tipo
        lote_origem = manejo.lote_origem
        lote_destino = manejo.lote_destino

        if tipo.exige_lote_origem and not lote_origem:
            raise ValidationError("O manejo exige um lote de origem.")

        if tipo.exige_lote_destino and not lote_destino:
            raise ValidationError("O manejo exige um lote de destino.")

        if tipo.move_lote and lote_origem == lote_destino:
            raise ValidationError("O lote de origem e destino devem ser diferentes para este tipo de manejo.")