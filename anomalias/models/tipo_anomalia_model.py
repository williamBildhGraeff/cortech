from django.db import models

class TipoAnomalia(models.Model):
 nome = models.CharField(max_length = 100)
 descricao = models.CharField(max_length = 100, blank = True, null = True)

 def __str__(self):
  return self.nome