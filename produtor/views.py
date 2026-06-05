from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .factories.produtor_factory import get_produtor_service
from .interfaces.produtor_interface import ProdutorInterface
from .serializers import ProdutorSerializer


class ProdutorViewSet(APIView):
     def __init__(self, service: ProdutorInterface = None, **kwargs):
       super().__init__(**kwargs)
       self.service = get_produtor_service()

     def get(self, request, produtor_id:int | None = None)-> Response:
        produtor = self.service.get(produtor_id)
        if produtor_id:
           serializer = ProdutorSerializer(produtor)
        else:
           serializer = ProdutorSerializer(produtor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

     def post(self, request):
        serializer = ProdutorSerializer(data=request.data)
        if serializer.is_valid():
           produtor = self.service.post(serializer.validated_data)
           return Response(ProdutorSerializer(produtor).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def put(self, request, produtor_id:int | None = None)-> Response:
        produtor = self.service.get(produtor_id)
        serializer = ProdutorSerializer(produtor, data=request.data)
        if serializer.is_valid():
           produtor = self.service.put(produtor_id, serializer.validated_data)
           return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, produtor_id:int | None = None)-> Response:
        self.service.delete(produtor_id)
        return Response(status=status.HTTP_204_NO_CONTENT)