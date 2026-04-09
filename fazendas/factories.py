from .services.fazenda_service import FazendaService

def get_fazenda_service() -> FazendaService:
    return FazendaService()