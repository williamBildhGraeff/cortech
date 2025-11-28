from django.db import models

# O models.py define como os dados são armazenados no banco de dados.
# Cada classe representa uma tabela, e cada atributo é uma coluna.

# 📦 Você coloca aqui:

# Campos (CharField, DateField, ForeignKey, etc.)

# Regras do banco (constraints, defaults)

# Métodos de negócio simples (__str__, cálculos, etc.)

class Endereco(models.Model):
 UF_CHOICES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
 ]
 logradouro = models.CharField(max_length = 100)
 numero = models.CharField(max_length = 10)
 bairro = models.CharField(max_length = 30)
 cidade = models.CharField(max_length = 100)
 uf = models.CharField(max_length = 2, choices = UF_CHOICES)
 cep = models.CharField(max_length = 9)

 def __str__(self):
  return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.uf}"

class Empresa(models.Model):
 nome = models.CharField(max_length = 100)
 cnpj = models.CharField(max_length = 30)
 endereco = models.ForeignKey(
  Endereco, 
  on_delete = models.CASCADE,
  )
 updated_at = models.DateTimeField(auto_now = True)
 def __str__(self):
  return self.nome
