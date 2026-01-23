from django.db import models
from usuarios.models import Usuario
class UsuarioEmpresa(models.Model):

 usuario = models.ForeignKey(
  Usuario,
  on_delete = models.CASCADE 
 )
 empresa = models.ForeignKey(
  "empresa.Empresa",
  on_delete = models.CASCADE
 )

 def __str__(self):
  return f"{self.usuario.nome} ({self.empresa.nome})"