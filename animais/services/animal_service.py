from animais.interfaces.animal_interface import AnimalInterface
from animais.models import Animal
from django.shortcuts import get_object_or_404

class AnimalService(AnimalInterface):
    def post(self, data):
        animal = Animal.objects.create(**data)
        self.score_rendimento(animal)
        return animal

    def get(self):
        return Animal.objects.all()

    def get_id(self, id):
        return Animal.objects.get(id=id)

    def put(self, id, data):
        animal = get_object_or_404(Animal, id=id)
        for key, value in data.items():
            setattr(animal, key, value)
        animal.save()
        return animal


    def delete(self, id):
        animal = get_object_or_404(Animal, id=id)
        animal.delete()
        return animal

    def score_rendimento(self, animal):
        score = animal.ganho_acumulado
        animal.score_rendimento = score
        animal.save()
        return animal
