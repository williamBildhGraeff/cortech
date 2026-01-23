from django.db import models

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

    STATUS_CHOICES = [
        ("ativo", "Ativo"),
        ("vendido", "Vendido"),
        ("morto", "Morto"),
        ("transferido", "Transferido"),
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

    brinco = models.CharField(max_length = 100, unique = True)
    sexo = models.CharField(max_length = 1, choices = SEXO_CHOICES, default = 'F')
    categoria = models.CharField(max_length = 20, choices = CATEGORIA_CHOICES, default = 'novilho')
    raca = models.CharField(max_length = 500, null = True, blank = True)
    origem = models.CharField(max_length = 20, choices = ORIGEM_CHOICES, default = 'compra')
    idade = models.CharField(max_length = 20, choices = IDADE_CHOICES, default = 'menor_12_meses')
    ganho_acumulado = models.FloatField(default = 0)
    score_rendimento = models.FloatField(default = 0)
    lote = models.ForeignKey(
        "lote.Lote",
        on_delete = models.CASCADE,
        related_name = 'animais'
    )
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default = 'ativo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Brinco {self.brinco} — {self.categoria}"
