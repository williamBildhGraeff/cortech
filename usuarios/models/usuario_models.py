
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from usuarios.managers import UsuarioManager

class Usuario(AbstractBaseUser, PermissionsMixin):

    TIPO_USUARIO = [
        ('admin', 'Administrador'),
        ('tecnico', 'Técnico'),
        ('produtor', 'Produtor')
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=TIPO_USUARIO)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    empresas = models.ManyToManyField(
        "empresa.Empresa",
        through="UsuarioEmpresa",
        related_name="usuarios"
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    def __str__(self):
        return self.email