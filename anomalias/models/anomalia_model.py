from django.db import models
from animais.models import Animal
from .tipo_anomalia_model import TipoAnomalia

class Anomalia(models.Model):
 animal = models.ForeignKey(
  Animal,
  on_delete = models.CASCADE,
  related_name = 'anomalias'
 )
 tipo = models.ForeignKey(
  TipoAnomalia,
  on_delete = models.CASCADE,
  related_name = 'anomalias'
 ),
 descricao = models.TextField(null = True, blank = True),
 data = models.DateTimeField(auto_now_add = True)
 
  # modelo = models.ForeignKey(
  #  ModeloTreinamento,
  #  on_delete=models.SET_NULL,
  #  null=True,
  #  blank=True,
  #  related_name="anomalias_detectadas"
  # )

 def __str__(self):
  return f"Anomalia - {self.tipo} - Animal {self.animal.brinco}"