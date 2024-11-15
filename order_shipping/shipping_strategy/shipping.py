from abc import ABC, abstractmethod

class Shipping(ABC):
    @abstractmethod
    def get_cost(self, order) -> float:
        pass

    @abstractmethod
    def get_date(self, order) -> str:
        pass