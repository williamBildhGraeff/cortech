from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usuarios.serializers.auth_serializer import LoginSerializer
from usuarios.services.auth_service import login_user


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = login_user(**serializer.validated_data)

        return Response(data, status=status.HTTP_200_OK)