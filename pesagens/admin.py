from django.contrib import admin
from .models import Pesagem

@admin.register(Pesagem)
class PesagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'data', 'peso', 'gmd_calculado_automatico', 'origem')
    list_filter = ('origem', 'data')
    search_fields = ('animal__brinco',)
