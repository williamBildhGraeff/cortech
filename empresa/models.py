from django.db import models
from endereco.models import Endereco
# O models.py define como os dados são armazenados no banco de dados.
# Cada classe representa uma tabela, e cada atributo é uma coluna.

# 📦 Você coloca aqui:

# Campos (CharField, DateField, ForeignKey, etc.)

# Regras do banco (constraints, defaults)

# Métodos de negócio simples (__str__, cálculos, etc.)

class Empresa(models.Model):
 nome = models.CharField(max_length = 100)
 cnpj = models.CharField(max_length = 30)
 endereco = models.ForeignKey(
  "endereco.Endereco", 
  on_delete = models.CASCADE,
  )
 updated_at = models.DateTimeField(auto_now = True)
 def __str__(self):
  return self.nome
