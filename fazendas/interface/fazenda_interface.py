from abc import ABC, abstractmethod

class FazendaInterface(ABC):
    
    @abstractmethod
    def post(self, data):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def put(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass