from django.db import models
from produtor.models import Produtor
from endereco.models import Endereco
# Create your models here.
class Fazenda(models.Model):
 nome = models.CharField(max_length = 100)
 produtor = models.ForeignKey(
  Produtor,
  on_delete = models.CASCADE
 )
 endereco = models.ForeignKey(
  Endereco,
  on_delete = models.CASCADE
 )
 create_at = models.DateTimeField(auto_now_add = True)
 update_at = models.DateTimeField(auto_now_add = True)

 def __str__(self): 
  return f"{self.nome} ({self.produtor.nome})"