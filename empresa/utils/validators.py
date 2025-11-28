import re
from rest_framework import serializers

def validar_cnpj(cnpj: str):
    cnpj_limpo = re.sub(r'\D', '', cnpj)

    if len(cnpj_limpo) != 14:
        raise serializers.ValidationError("CNPJ deve ter 14 dígitos.")

    # Aqui você pode implementar a validação real dos dígitos verificadores
    # ou usar uma lib como `validate-docbr`
    return cnpj_limpo


def validar_cep(cep: str):
    if not re.match(r'^\d{5}-?\d{3}$', cep):
        raise serializers.ValidationError("CEP inválido.")
    return cep