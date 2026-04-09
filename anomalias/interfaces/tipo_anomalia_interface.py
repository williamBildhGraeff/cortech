from abc import ABC, abstractmethod

class TipoAnomaliaInterface(ABC):
    @abstractmethod
    def get(self, id=None):
        pass

    @abstractmethod
    def post(self, data):
        pass

    @abstractmethod
    def put(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass