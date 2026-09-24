from django.urls import path
from .views import AnimalView

urlpatterns = [
    path('<int:lote_id>/animais/', AnimalView.as_view(), name='animais'),
    path('animais/<int:id>/', AnimalView.as_view(), name='animais'),
]