from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


def login_user(email, password, empresa_id):
    user = authenticate(email=email, password=password)

    if user is None:
        raise AuthenticationFailed("Credenciais inválidas")

    if not user.empresas.filter(id=empresa_id).exists():
        raise AuthenticationFailed("Usuário não pertence a essa empresa")

    refresh = RefreshToken.for_user(user)
    refresh["empresa_id"] = empresa_id
    refresh["role"] = user.role

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "usuario": {
            "id": user.id,
            "nome": user.nome,
            "email": user.email,
            "role": user.role,
            "empresa_id": empresa_id,
        }
    }