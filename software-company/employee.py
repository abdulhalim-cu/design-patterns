from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def perform_duties(self):
        pass
