from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..factories.pesagem_factory import get_pesagem_service
from ..interfaces.pesagens_interface import PesagemInterface
from ..serializer import PesagemSerializer, PesagemIndicadoresSerializer


class PesagemViewSet(APIView):
   def __init__(self, service: PesagemInterface = None, **kwargs):
      super().__init__(**kwargs)
      self.service = service or get_pesagem_service()

   def get(self, request, animal_id:int | None = None, lote_id:int | None = None) -> Response:
      if animal_id:
         dados = self.service.get(animal_id=animal_id)
         indicadores_serializer = PesagemIndicadoresSerializer(dados['indicadores'])
         pesagens_serializer = PesagemSerializer(dados['pesagens'], many=True)
         resposta = {
            'indicadores': indicadores_serializer.data,
            'pesagens': pesagens_serializer.data
         }
      else:
         dados = self.service.get(lote_id=lote_id)
         serializer = PesagemSerializer(dados['pesagens'], many=True)
         resposta = {
            'pesagens': serializer.data,
            'analise': dados['analise']
         }
      return Response(resposta, status=status.HTTP_200_OK)

   def put(self, request, pesagem_id: int) -> Response:

      serializer = PesagemSerializer(
         data=request.data,
         partial=True
      )

      serializer.is_valid(
         raise_exception=True
      )

      print(serializer.validated_data)
      pesagem = self.service.put(
         pesagem_id,
         serializer.validated_data
      )

      return Response(PesagemSerializer(pesagem).data, status=status.HTTP_200_OK)

   def delete(self, request, pesagem_id: int) -> Response:
      self.service.delete(pesagem_id)
      return Response(status=status.HTTP_204_NO_CONTENT)


   def post(self, request, animal_id:int = None) -> Response:
      serializer = PesagemSerializer(data=request.data)
      if serializer.is_valid():
        pesagem = self.service.post(serializer.validated_data)
        return Response(PesagemSerializer(pesagem).data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
