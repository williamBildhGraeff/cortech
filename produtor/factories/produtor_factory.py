from produtor.interfaces.produtor_interface import ProdutorInterface
from produtor.services.produtor_service import ProdutorService


def get_produtor_service() -> ProdutorInterface:
    return ProdutorService()