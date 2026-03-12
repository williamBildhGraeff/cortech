from abc import ABC, abstractmethod

class AnimalInterface(ABC):
    @abstractmethod
    def post(self, data):
        pass

    @abstractmethod
    def get(self): 
        pass
    
    @abstractmethod
    def get_id(self, id):
        pass

    @abstractmethod
    def put(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass