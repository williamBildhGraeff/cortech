from .services.service_anomalia import AnomaliaService
from .interfaces.anomalia_interface import AnomaliaInterface
from .services.service_tipo_anomalia import TipoAnomaliaService
from .interfaces.tipo_anomalia_interface import TipoAnomaliaInterface

def get_anomalia_service() -> AnomaliaInterface:
    return AnomaliaService()

def get_tipo_anomalia_service() -> TipoAnomaliaInterface:
    return TipoAnomaliaService()