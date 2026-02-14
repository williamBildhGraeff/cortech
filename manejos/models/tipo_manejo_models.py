from django.db import models

class TipoManejo(models.Model):
    nome = models.CharField(max_length = 100, unique = True)
    descricao = models.TextField(null = True, blank = True)
    move_lote = models.BooleanField(default=False)
    exige_lote_origem = models.BooleanField(default=False)
    exige_lote_destino = models.BooleanField(default=False)

def __str__(self):
    return self.nome