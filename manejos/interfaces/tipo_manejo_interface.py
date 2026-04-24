from abc import ABC, abstractmethod


class TipoManejoInterface(ABC):
    @abstractmethod
    def get(self, tipomanejoid:int | None = None):
        pass
    @abstractmethod
    def post(self, data):
        pass

    @abstractmethod
    def put(self, tipomanejoid:int, data):
        pass

    @abstractmethod
    def delete(self, tipomanejoid:int):
        pass