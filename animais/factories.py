from .services.animal_service import AnimalService
from .interfaces.animal_interface import AnimalInterface

def get_animal_service() -> AnimalInterface:
    return AnimalService()
    