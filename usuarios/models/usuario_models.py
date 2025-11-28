from django.db import models
from empresa.models import Empresa
from django.contrib.auth.hashers import make_password

# Create your models here.
class Usuario(models.Model):
 TIPO_USUARIO = [
  ('admin', 'Administrador'),
  ('tecnico', 'Técnico'),
  ('produtor', 'Produtor')
 ]
 nome = models.CharField(max_length = 100)
 email = models.CharField(max_length = 100) 
 senha_hash = models.CharField(max_length = 100)
 empresa = models.ForeignKey(
  Empresa,
  on_delete = models.CASCADE,
  blank = False,
  null = False
 )
 role = models.CharField(max_length = 8, choices=TIPO_USUARIO)

 def __str__(self):
  return f"{self.nome}"

 def save(self, *args, **kwargs):
  if not self.senha_hash.startswith('pbkdf2_'):
   self.senha_hash = make_password(self.senha_hash)
  super().save(*args, **kwargs)