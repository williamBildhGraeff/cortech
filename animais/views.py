from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal
from .serializer import AnimalSerializer
from .services.animal_service import AnimalService
from rest_framework import status

class AnimalView(APIView):
    service = AnimalService()
    def get(self, request, id=None):
        print(f'id: {id}')
        if id: 
            animal = self.service.get_id(id)
            animal_serializer = AnimalSerializer(animal)
            return Response(animal_serializer.data, status=status.HTTP_200_OK)
        animais = self.service.get()
        serializer = AnimalSerializer(animais, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request): 
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            animal = self.service.post(serializer.validated_data)
            return Response(AnimalSerializer(animal).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        animal = self.service.get_id(id)
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            animal = self.service.put(id,serializer.validated_data)
            return Response(AnimalSerializer(animal).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        animal = self.service.delete(id)
        return Response(AnimalSerializer(animal).data, status=status.HTTP_200_OK)
    
    def get_id(self, request,id):
        animal = self.service.get_id(id)
        return Response(AnimalSerializer(animal).data, status=status.HTTP_200_OK)