# Create your models here.
from django.db import models


class Produtor(models.Model):
 nome = models.CharField(max_length = 100)
 cpf_cnpj = models.CharField(max_length=18, unique=True)
 telefone = models.CharField(max_length = 20)
 email = models.EmailField(blank = True, null = True)
 empresa = models.ForeignKey(
  "empresa.Empresa",
  on_delete=models.CASCADE,
  related_name="produtores"
 )
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.nome


















