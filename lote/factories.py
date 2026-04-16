from .interfaces.lote_interface import LoteInterface
from .services.lote_service import LoteService

def get_lote_service() -> LoteInterface:
    return LoteService()