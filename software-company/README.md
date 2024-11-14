# Software Company

This project demonstrates a simple software company structure using principles of object-oriented programming and design patterns. The primary focus is on creating a flexible, loosely coupled system by using an interface for different employee roles and defining specific company types that can have varying employee compositions.

## Overview

The project consists of the following components:
- `Employee` interface: Defines a generic `perform_duties` method that all roles must implement.
- Specific Employee Roles (`Designer`, `Programmer`, `Tester`, and `Artist`): Implement the `Employee` interface and define their own responsibilities.
- `Company` class: The base company class that manages employees and their duties through the `Employee` interface.
- Specific Company Types (`GameDevCompany` and `OutsourcingCompany`): These subclasses of `Company` create different sets of employees based on their specific needs.

## Structure

### Employee Interface

The `Employee` interface defines a `perform_duties` method, which is a generic operation that each employee must implement. Each specific role (Designer, Programmer, Tester, Artist) implements this interface and defines its own version of `perform_duties`.

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def perform_duties(self):
        pass
```

### Specific Employee Roles

Each employee class implements the `Employee` interface and defines unique methods to represent the specific responsibilities of that role (e.g., `design_architecture` for Designer, `write_code` for Programmer, `test_software` for Tester). The `perform_duties` method calls these unique methods.

```python
class Designer(Employee):
    def perform_duties(self):
        self.design_architecture()

    def design_architecture(self):
        print("Designer is designing the architecture.")

class Programmer(Employee):
    def perform_duties(self):
        self.write_code()

    def write_code(self):
        print("Programmer is writing code.")

class Tester(Employee):
    def perform_duties(self):
        self.test_software()

    def test_software(self):
        print("Tester is testing the software.")

class Artist(Employee):
    def perform_duties(self):
        self.create_graphics()

    def create_graphics(self):
        print("Artist is creating graphics.")
```

### Base Company Class

The `Company` class works with a list of `Employee` objects and manages the creation of software by calling `perform_duties` on each employee. The `Company` class has an abstract `get_employees` method that is overridden in subclasses to specify the employees for each specific company type.

```python
from abc import ABC, abstractmethod

class Company(ABC):
    def create_software(self):
        employees = self.get_employees()
        for employee in employees:
            employee.perform_duties()

    @abstractmethod
    def get_employees(self):
        pass
```

### Specific Company Types

The `GameDevCompany` and `OutsourcingCompany` classes are concrete implementations of the `Company` class. Each one overrides the `get_employees` method to define a different set of employees, reflecting their unique team compositions.

```python
class GameDevCompany(Company):
    def get_employees(self):
        return [Designer(), Artist()]

class OutsourcingCompany(Company):
    def get_employees(self):
        return [Programmer(), Tester()]
```

## Example Usage

You can create instances of `GameDevCompany` and `OutsourcingCompany` and call `create_software` to see how each company type works with its specific set of employees.

```python
game_dev_company = GameDevCompany()
outsourcing_company = OutsourcingCompany()

print("GameDevCompany is creating software:")
game_dev_company.create_software()

print("\nOutsourcingCompany is creating software:")
outsourcing_company.create_software()
```

## Benefits of This Structure

- **Single Interface for Multiple Roles**: By using a common `Employee` interface, the `Company` class can manage different types of employees uniformly.
- **Flexible Team Composition**: Specific company types can define their own teams by implementing the `get_employees` method. This allows different company structures without modifying the core logic.
- **Open for Extension**: New roles (e.g., ProductManager) or company types can be added by simply implementing `Employee` or extending `Company`. This follows the Open/Closed Principle, allowing easy expansion without altering existing classes.
- **Loose Coupling**: The `Company` class interacts only with the `Employee` interface, not specific classes, promoting flexibility and maintainability.
- **Factory-like Employee Creation**: The `get_employees` method acts as a factory, allowing each `Company` subclass to generate its own employees as needed.

This improved architecture makes the project more extensible, modular, and adaptable to different types of companies and employee roles.
