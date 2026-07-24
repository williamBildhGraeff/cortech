from django.db import models
# Create your models here.
class Fazenda(models.Model):
 nome = models.CharField(max_length=100)
 codigo = models.CharField(max_length=50, unique=True, null=True, blank=True)

 produtor = models.ForeignKey(
  "produtor.Produtor",
  on_delete=models.CASCADE,
  related_name="fazendas"
 )

 endereco = models.ForeignKey(
  "endereco.Endereco",
  on_delete=models.CASCADE
 )

 area_total_hectares = models.DecimalField(
  max_digits=10,
  decimal_places=2,
  null=True,
  blank=True
 )
 status = models.CharField(
  max_length=20,
  choices=[
   ("ativa", "Ativa"),
   ("inativa", "Inativa"),
   ("venda", "À venda"),
  ],
  default="ativa"
 )

 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.nome