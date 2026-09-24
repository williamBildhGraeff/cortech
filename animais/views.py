from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal
from .serializer import AnimalSerializer
from .interfaces.animal_interface import AnimalInterface
from .factories import get_animal_service
from rest_framework import status

class AnimalView(APIView):
    def __init__(self, service: AnimalInterface = None, **kwargs):
        super().__init__(**kwargs)
        self.service = service or get_animal_service()

    def get(self, request, id=None, lote_id=None):
        animal = self.service.get(id, lote_id)
        if id: 
            serializer = AnimalSerializer(animal)
        else:
            serializer = AnimalSerializer(animal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self,request, lote_id=None):
        request.data['lote'] = lote_id
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            animal = self.service.post(serializer.validated_data)
            return Response(AnimalSerializer(animal).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, lote_id=None):
        animal = self.service.get(id)
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            animal = self.service.put(id, serializer.validated_data)
            return Response(AnimalSerializer(animal).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id:int=None, lote_id=None):
        self.service.delete(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    