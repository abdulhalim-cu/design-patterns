# Software Company

This project demonstrates a simple software company structure using the principles of object-oriented programming and design patterns. The main focus is on decoupling the code by using an interface for different employee roles.

## Overview

The project consists of the following components:
- `Employee` interface: Defines a generic `perform_duties` method that all roles must implement.
- `Designer`, `Programmer`, and `Tester` classes: Implement the `Employee` interface and define their specific responsibilities.
- `Company` class: Works with the `Employee` interface to manage different types of employees and their duties.

## Structure

### Employee Interface

The `Employee` interface defines a `perform_duties` method, which is the generic operation each employee can perform. Each specific role (Designer, Programmer, Tester) implements this interface and defines its own version of `perform_duties`.

```python

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def perform_duties(self):
        pass
```

## Specific Roles
Each class (Designer, Programmer, Tester) implements the Employee interface and defines its unique method (design_architecture, write_code, test_software), which is called within perform_duties.

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
```

## Company Class
The Company class takes a list of Employee objects (which can include any type of employee, as long as they implement Employee). In the create_software method, the Company class calls perform_duties on each employee in the list, without needing to know the specific type of each employee.

```python
class Company:
    def __init__(self, employees):
        self.employees = employees

    def create_software(self):
        for employee in self.employees:
            employee.perform_duties()
```

## Example Usage
You create instances of Designer, Programmer, and Tester, and pass them as a list to the Company. The Company can then call perform_duties on each employee, which delegates to each employee’s specific method.

```python
    designer = Designer()
    programmer = Programmer()
    tester = Tester()

    company = Company([designer, programmer, tester])
    company.create_software()
```
## Benefits of This Structure
- Single Interface for Multiple Roles: By using a common Employee interface, the Company class can handle different types of employees uniformly.
- Open for Extension: If new roles (e.g., ProductManager) are added, they just need to implement Employee, and the Company class can automatically handle them without modification.
- Loose Coupling: The Company class is now loosely coupled with the roles. It depends on the Employee interface rather than specific classes, which increases flexibility and maintainability.

This approach makes the architecture more extensible and modular, as new employee types can be added without altering the Company class, following the Open/Closed Principle in software design