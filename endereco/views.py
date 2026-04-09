from rest_framework import viewsets
from endereco.models import Endereco
from endereco.serializer import EnderecoSerializer
from .service import get_endereco_service
from .interface import EnderecoInterface
# Create your views here.
class EnderecoViewSet(viewsets.ModelViewSet):
  def __init__(self, service: EnderecoInterface = None, **kwargs):
      super().__init__(**kwargs)
      self.service = service or get_endereco_service() 

  def get(self, request, id=None):
    endereco = self.service.get(id)
    if id:
      serializer = EnderecoSerializer(request)
    else:
      serializer = EnderecoSerializer(request, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = EnderecoSerializer(data=request.data)
    if serializer.is_valid():
      endereco = self.service.post(request)
      return Response(EnderecoSerializer(endereco).data, status=status.HTTP_201_CREATED)

  def put(self, request, id):
    endereco = self.service.get(id=id)
    serializer = EnderecoSerializer(endereco, reuqest.data)
    if serializer.is_valid():
      endereco = self.service.put(id, endereco.validated_data) 
      return Response(EnderecoSerializer(endereco).data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, id):
    self.service.delete(id)
    return Response(status=status.HTTP_204_OK)
