from abc import ABC, abstractmethod

class AnimalInterface(ABC):
    @abstractmethod
    def post(self, data, lote_id=None):
        pass

    @abstractmethod
    def get(self, id=None, lote_id=None):
        pass

    @abstractmethod
    def put(self, id, data, lote_id=None):
        pass

    @abstractmethod
    def delete(self, id, lote_id=None):
        pass