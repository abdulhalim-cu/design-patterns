from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def get_nutrition(self):
        raise NotImplementedError("Subclasses must implement get_nutrition")

    @abstractmethod
    def get_color(self):
        raise NotImplementedError("Subclasses must implement get_color")

    @abstractmethod
    def get_expiration(self):
        raise NotImplementedError("Subclasses must implement get_expiration")
