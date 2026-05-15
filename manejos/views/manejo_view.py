from rest_framework.response import Response
from rest_framework.views import APIView

from ..factories import get_manejo_service
from ..interfaces.manejo_interface import ManejoInterface
from ..serializers import ManejoSerializer
from rest_framework import status


class ManejoViewSet(APIView):
  def __init__(self, service: ManejoInterface = None, **kwargs):
    super().__init__(**kwargs)
    self.service = service or get_manejo_service()

  def get(self, request, manejoid:int | None = None) -> Response:
    manejo = self.service.get(manejoid)
    if manejoid:
      serializer = ManejoSerializer(manejo)
    else:
      serializer = ManejoSerializer(manejo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request) -> Response:
    serializer = ManejoSerializer(data=request.data)
    if serializer.is_valid():
      manejo = self.service.post(serializer.validated_data)
      return Response(ManejoSerializer(manejo).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

