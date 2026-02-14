from django.db import models

class Manejo(models.Model):
    tipo = models.ForeignKey(
        "manejos.TipoManejo",
        on_delete=models.CASCADE,
        related_name='manejos'
    )

    data = models.DateField(auto_now_add=True)
    observacao = models.TextField(null=True, blank=True)

    lote_origem = models.ForeignKey(
        "lote.Lote",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='manejos_origem'
    )

    lote_destino = models.ForeignKey(
        "lote.Lote",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='manejos_destino'
    )

    animais = models.ManyToManyField(
        "animais.Animal",
        related_name='manejos'
    )

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
  return f'{self.tipo.nome} | {self.animais.count()} animais | {self.data}'