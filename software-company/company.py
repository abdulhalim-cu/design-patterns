from abc import ABC, abstractmethod


class Company(ABC):
    def create_software(self):
        employees = self.get_employees()
        for employee in employees:
            employee.perform_duties()

    @abstractmethod
    def get_employees(self):
        pass
