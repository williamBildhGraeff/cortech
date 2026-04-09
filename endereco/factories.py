from .interfaces import EnderecoInterface
from .services import EnderecoService
def get_endereco_factories() -> EnderecoInterface:
    return EnderecoService()
