from django.urls import path
from usuarios.views.auth_views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view()),
]