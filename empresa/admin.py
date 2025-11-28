# Register your models here.
from django.contrib import admin
from .models import Empresa, Endereco

admin.site.register(Empresa)
admin.site.register(Endereco)