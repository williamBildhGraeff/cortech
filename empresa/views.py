from rest_framework.views import APIView
from .models import Empresa
from .serializer import EmpresaSerializer
from .factories import get_empresa_service
from .interface.interface_empresa import EmpresaInterface
from rest_framework import status
from rest_framework.response import Response

class EmpresaViewSet(APIView):
    def __init__(self, service: EmpresaInterface = None, **kwargs):
        super().__init__(**kwargs)
        self.service = service or get_empresa_service()

    def get(self, request, id=None):
        empresa = self.service.get(id)
        if id:
            serializer = EmpresaSerializer(empresa)
        else: 
            serializer = EmpresaSerializer(empresa, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            empresa = self.service.post(serializer.validated_data)
            return Response(EmpresaSerializer(empresa).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        empresa = self.service.get(id)
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            empresa = self.service.put(id,serializer.validated_data)
            return Response(EmpresaSerializer(empresa).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        empresa = self.service.delete(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
#  ViewSet da Empresa controla todas as operações CRUD da tabela.
#  - Utiliza o EmpresaSerializer para validar dados
#  - Retorna JSON para o front-end
# 
 