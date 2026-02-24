from django.db import models

class UsuarioEmpresa(models.Model):
    usuario = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    empresa = models.ForeignKey("empresa.Empresa", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("usuario", "empresa")

    def __str__(self):
        return f"{self.usuario.email} - {self.empresa.nome}"