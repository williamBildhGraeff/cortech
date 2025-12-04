from django.db import models
from lote.models import Lote

class Animal(models.Model):
 SEXO_CHOICES = [
  ('M', 'Macho'),
  ('F', 'Femea')
 ]

 CATEGORIA_CHOICES = [
  ("bezerro", "Bezerro"),
  ("novilho", "Novilho"),
  ("vaca", "Vaca"),
  ("touro", "Touro"),
 ]

 ORIGEM_CHOICES = [
  ("compra", "Compra"),
  ("nascimento", "Nascimento"),
  ("terceiros", "Terceiros"),
 ]

 IDADE_CHOICES = [
  ("maior_12_meses", "Maior que 12 meses"),
  ("menor_12_meses", "Menor que 12 meses")
 ]

 brinco = models.CharField(max_length = 100)
 sexo = models.CharField(max_length = 1, choices = SEXO_CHOICES, default = 'F')
 categoria = models.CharField(max_length = 20, choices = CATEGORIA_CHOICES, default = 'novilho')
 raca = models.CharField(max_length = 500, null = True, blank = True)
 origem = models.CharField(max_length = 20, choices = ORIGEM_CHOICES, default = 'compra')
 idade = models.CharField(max_length = 20, choices = IDADE_CHOICES)
 ganho_acumulado = models.FloatField(default = 0)
 score_rendimento = models.FloatField(default = 0)
 lote = models.ForeignKey(
  Lote,
  on_delete = models.CASCADE,
  related_name = 'animais'
 )
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 def __str__(self):
  return f"Brinco {self.brinco} — {self.categoria}"
