from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


def login_user(email, password):
    user = authenticate(
        email=email,
        password=password,
    )

    if user is None:
        raise AuthenticationFailed(
            "Usuário e/ou senha inválidos."
        )

    refresh = RefreshToken.for_user(user)
    refresh["role"] = user.role

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "usuario": {
            "id": user.id,
            "nome": user.nome,
            "email": user.email,
            "role": user.role
        },
        "empresas": [
            {
                "id": emp.id,
                "nome": emp.nome,
            }
            for emp in user.empresas.all()
        ]
    }