from abc import ABC, abstractmethod


class PesagemInterface(ABC):
    @abstractmethod
    def post(self, pesagem:dict, animal_id:int = None):
        pass

    @abstractmethod
    def get(self, lote_id:int, animal_id:int):
        pass

    @abstractmethod
    def put(self, pesagem_id:int, pesagem:dict):
        pass

    @abstractmethod
    def delete(self, pesagem_id:int):
        pass