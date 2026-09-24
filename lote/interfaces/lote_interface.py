from abc import ABC, abstractmethod

class LoteInterface(ABC):
    @abstractmethod
    def get(self, id = None, fazenda_id = None):
        pass
    
    @abstractmethod
    def post(self, data, produtor_id = None):
        pass

    @abstractmethod
    def put(self, id, data, produtor_id = None):
        pass

    @abstractmethod
    def delete(self, id, produtor_id = None):
        pass