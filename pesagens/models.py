from django.db import models
from animais.models import Animal
from django.utils import timezone

class Pesagem(models.Model):
 ORIGEM_CHOICES = (
  ('manual', 'Manual'),
  ('importacao', 'Importação'),
 )
 animal = models.ForeignKey(
  Animal,
  on_delete = models.CASCADE,
  related_name = 'pesagens'
 )
 data = models.DateField(default = timezone.now)
 peso = models.DecimalField(max_digits = 6, decimal_places = 2)
 gmd_calculado_automatico = models.DecimalField(max_digits = 6, decimal_places = 2, null = True, blank = True)
 origem = models.CharField(max_length = 20, choices = ORIGEM_CHOICES, default = 'manual')
 def __str__(self):
  return f"{self.animal.brinco} - {self.peso} kg ({self.data})"

 def save(self, *args, **kwargs):
  ultima = Pesagem.objects.filter(
   animal=self.animal,
   data__lt=self.data        # <-- CORRETO
  ).order_by('-data').first()
  if ultima:
   dias = (self.data - ultima.data).days
   if dias > 0:
    ganho = float(self.peso) - float(ultima.peso)
    self.gmd_calculado_automatico = ganho / dias

  super().save(*args, **kwargs)
