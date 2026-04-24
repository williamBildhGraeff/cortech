from manejos.services.manejo_service import ManejoService
from manejos.services.tipo_manejo import TipoManejoService

def get_tipo_manejo_service()->TipoManejoService:
    return TipoManejoService()

def get_manejo_service()->ManejoService:
    return ManejoService()