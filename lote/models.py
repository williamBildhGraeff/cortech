from django.db import models
from fazendas.models import Fazenda

class Lote(models.Model):
 STATUS = [
  ('ativo', 'Ativo'),
  ('Fechado', 'Fechado'),
  ('vendido', 'Vendido')
 ]
 nome = models.CharField(max_length = 100)
 data_entrada = models.DateField()
 data_saida = models.DateField(null = True, blank = True)
 peso_medio = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
 gmd_medio = models.DecimalField(max_digits = 10, decimal_places = 3, null = True, blank = True) 
 raca_majoritaria = models.CharField(max_length = 100, null = True, blank = True)
 status = models.CharField(max_length = 100, choices = STATUS, default = 'ativo')
 fazenda = models.ForeignKey(
  Fazenda,
  on_delete = models.CASCADE,
  related_name = 'lotes'
 )
 created_at = models.DateTimeField(auto_now_add = True)
 updated_at = models.DateField(auto_now = True)

 def __str__(self):
  return f"{self.nome} ({self.fazenda.nome})"
