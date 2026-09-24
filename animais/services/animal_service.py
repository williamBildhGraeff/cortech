from animais.interfaces.animal_interface import AnimalInterface
from animais.models import Animal
from django.shortcuts import get_object_or_404

class AnimalService(AnimalInterface):
    def post(self, data, lote_id=None):
        animal = Animal.objects.create(**data)
        self.score_rendimento(animal)
        return animal

    def get(self, id=None, lote_id=None):
        if id:
            return get_object_or_404(Animal, id=id)
        return Animal.objects.all()

    def put(self, id, data, lote_id=None):
        animal = self.get(id=id)
        for key, value in data.items():
            setattr(animal, key, value)
        animal.save()
        return animal


    def delete(self, id, lote_id=None):
        animal = self.get(id=id)
        animal.delete()

    def score_rendimento(self, animal):
        score = animal.ganho_acumulado
        animal.score_rendimento = score
        animal.save()
        return animal
