# Create your models here.
from django.db import models


class Produtor(models.Model):
 nome = models.CharField(max_length = 100)
 cpf_cnpj = models.CharField(max_length = 18)
 telefone = models.CharField(max_length = 20)
 email = models.EmailField(blank = True, null = True)
 usuario = models.ForeignKey(
  "usuarios.Usuario",
  on_delete = models.CASCADE,

 )

 def __str__(self):
  return self.nome