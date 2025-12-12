from django.db import models
from animais.models import Animal
from lote.models import Lote
from .tipo_manejo_models import TipoManejo

class Manejo(models.Model):
 animal = models.ForeignKey(
  Animal,
  on_delete = models.CASCADE,
  related_name = 'manejos'
 )
 tipo = models.ForeignKey(
  TipoManejo,
  on_delete = models.CASCADE,
  related_name = 'manejos'
 )
 observacao = models.TextField(null = True, blank = True)
 data = models.DateField()
 peso = models.FloatField(null = True, blank = True)

 lote = models.ForeignKey(
  Lote,
  on_delete = models.SET_NULL,
  null = True,
  blank = True
 )

 def save(self, *args, **kwargs):
  self.lote = self.animal.lote
  super().save(*args, **kwargs)

 def __str__(self):
  tipo_nome = self.tipo.nome if self.tipo else "Sem Tipo"
  return f'{self.tipo.nome} - Animal {self.animal.brinco} - {self.data}'