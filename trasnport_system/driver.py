from abc import ABC, abstractmethod


class Driver(ABC):
    @abstractmethod
    def navigate(self):
        pass
