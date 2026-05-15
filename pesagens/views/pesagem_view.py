from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..factories.pesagem_factory import get_pesagem_service
from ..interfaces.pesagens_interface import PesagemInterface
from ..serializer import PesagemSerializer


class PesagemViewSet(APIView):
   def __init__(self, service: PesagemInterface = None, **kwargs):
      super().__init__(**kwargs)
      self.service = service or get_pesagem_service()

   def get(self, request, pesagem_id:int | None = None) -> Response:
      dados = self.service.get(pesagem_id)
      if pesagem_id:
         serializer = PesagemSerializer(dados)
      else:
         serializer = PesagemSerializer(dados, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

   def post(self, request) -> Response:
      serializer = PesagemSerializer(data=request.data)
      if serializer.is_valid():
        pesagem = self.service.post(serializer.validated_data)
        return Response(PesagemSerializer(pesagem).data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
