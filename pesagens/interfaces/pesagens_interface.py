from abc import ABC, abstractmethod


class PesagemInterface(ABC):
    @abstractmethod
    def post(self, pesagem:dict):
        pass

    @abstractmethod
    def get(self):
        pass

    # @abstractmethod
    # def put(self, pesagem:dict):
    #     pass
    #
    # @abstractmethod
    # def delete(self, pesagem_id:int):
    #     pass