from abc import ABC, abstractmethod

from rest_framework.response import Response


class ManejoInterface(ABC):
    @abstractmethod
    def get(self, manejoid:int | None = None):
        pass
    
    @abstractmethod
    def post(self, data: dict):
        pass