from abc import abstractmethod, ABC

class ProdutorInterface(ABC):
    @abstractmethod
    def get(self, produtor_id:int | None = None):
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