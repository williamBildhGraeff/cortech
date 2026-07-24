from abc import ABC, abstractmethod

class FazendaInterface(ABC):
    
    @abstractmethod
    def post(self, data, produtor_id):
        pass

    @abstractmethod
    def get(self, id, produtor_id):
        pass

    @abstractmethod
    def put(self, id, data, produtor_id):
        pass

    @abstractmethod
    def delete(self, id, produtor_id):
        pass