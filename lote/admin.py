from django.contrib import admin
from .models import Lote
# Register your models here.
@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'fazenda', 'status', 'data_entrada', 'data_saida')
    list_filter = ('status', 'fazenda')
    search_fields = ('nome',)