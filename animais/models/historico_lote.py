from django.db import models
from django.utils import timezone


class HistoricoLoteAnimal(models.Model):
    ORIGEM_CHOICES = [
        ("manual", "Manual"),
        ("importacao", "Importação"),
    ]

    animal = models.ForeignKey("animais.Animal", on_delete=models.CASCADE)
    lote_origem = models.ForeignKey(
        "lote.Lote",
        on_delete=models.PROTECT,
        related_name="historico_como_origem",
    )
    lote_destino = models.ForeignKey(
        "lote.Lote",
        on_delete=models.PROTECT,
        related_name="historico_como_destino",
    )
    data = models.DateField()
    origem = models.CharField(max_length=20, choices=ORIGEM_CHOICES, default="manual")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-data", "-created_at"]
        indexes = [
            models.Index(fields=["animal", "data"]),
            models.Index(fields=["lote_origem"]),
            models.Index(fields=["lote_destino"]),
        ]
        verbose_name_plural = "Históricos de Lote de Animais"
    
    def clean(self):
        if self.lote_origem == self.lote_destino:
            raise ValidationError("Lote origem e destino não podem ser iguais.")

    def __str__(self):
        return f"{self.animal.brinco} {self.lote_origem} → {self.lote_destino}"