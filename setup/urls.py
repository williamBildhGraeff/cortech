from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('empresa.urls')),
    path('api/', include('usuarios.urls')),
    path('api/', include('produtor.urls')),
    path('api/', include('fazendas.urls')),
    path('api/', include('lote.urls')),
    path('api/', include('animais.urls')),
    path('api/', include('pesagens.urls'))
]
