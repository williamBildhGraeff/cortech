from empresa.service.empresa_service import EmpresaService
from empresa.interface.interface_empresa import EmpresaInterface

def get_empresa_service() -> EmpresaInterface:
    return EmpresaService()