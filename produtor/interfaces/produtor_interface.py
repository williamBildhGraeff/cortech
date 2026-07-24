from abc import abstractmethod, ABC

from rest_framework.response import Response


class ProdutorInterface(ABC):
    @abstractmethod
    def get(self, produtor_id:int | None = None, empresa_id:int | None = None)-> Response:
        pass

    @abstractmethod
    def post(self, produtor:dict):
        pass

    @abstractmethod
    def put(self, produtor_id:int, produtor:dict):
        pass

    @abstractmethod
    def delete(self, produtor_id:int):
        pass