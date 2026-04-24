from rest_framework.response import Response
from rest_framework.views import APIView

from ..factories import get_tipo_manejo_service
from ..interfaces.tipo_manejo_interface import TipoManejoInterface
from ..serializers import TipoManejoSerializer
from rest_framework import status

class TipoManejoViewSet(APIView):
  def __init__(self, service: TipoManejoInterface = None, **kwargs):
    super().__init__(**kwargs)
    self.service = service or get_tipo_manejo_service()

  def get(self, request, tipomanejoid:int | None = None) -> Response:
    tipomanejo = self.service.get(tipomanejoid)
    if tipomanejoid:
      serializer = TipoManejoSerializer(tipomanejo)
    else:
      serializer = TipoManejoSerializer(tipomanejo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request) -> Response:
    serializer = TipoManejoSerializer(data=request.data)
    if serializer.is_valid():
      tipomanejo = self.service.post(serializer.validated_data)
      return Response(TipoManejoSerializer(tipomanejo).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, tipomanejoid:int) -> Response:
    tipomanejo = self.service.get(tipomanejoid)
    serializer = TipoManejoSerializer(tipomanejo, data=request.data)
    if serializer.is_valid():
      tipomanejo = self.service.put(tipomanejoid, serializer.validated_data)
      return Response(TipoManejoSerializer(tipomanejo).data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, tipomanejoid:int) -> Response:
    self.service.delete(tipomanejoid)
    return Response(status=status.HTTP_204_NO_CONTENT)