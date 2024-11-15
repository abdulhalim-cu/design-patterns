# Transport System using Composition Design Pattern

This project implements a flexible `Transport` system using the **Composition Design Pattern**. The pattern separates the responsibilities of different components (like `Engine` and `Driver`), allowing them to be composed dynamically. This approach improves flexibility and promotes reusability, as the `Transport` class can work with different types of engines and drivers without needing modifications.

## Design Overview

The project uses the **Composition Design Pattern** to decouple various behaviors (e.g., `move` and `navigate`) from the `Transport` class. Rather than inheriting specific behaviors, the `Transport` class delegates them to separate classes (`Engine` and `Driver`), making it easy to change or extend behaviors independently.

## Structure

### 1. `Transport` Class

The `Transport` class represents a vehicle that depends on two components:
- **Engine**: Responsible for the movement.
- **Driver**: Responsible for navigation.

The `Transport` class uses composition to work with instances of `Engine` and `Driver`, enabling the transport to have various combinations of engines and drivers.

```python
class Transport:
    def __init__(self, driver, engine):
        self.engine = engine
        self.driver = driver

    def deliver(self, destination, cargo):
        print(f"Starting delivery of {cargo} to {destination}.")
        self.driver.navigate(destination)
        self.engine.move()
        print(f"Delivery of {cargo} to {destination} completed.")
```

### 2. `Engine` Interface

The `Engine` interface defines the `move` behavior. Each engine type (e.g., `CombustionEngine`, `ElectricEngine`) implements this interface, providing its specific movement behavior.

```python
class Engine(ABC):
    @abstractmethod
    def move(self):
        pass
```

#### Implementations:
- **CombustionEngine**: Moves using fuel-based power.
- **ElectricEngine**: Moves using electric power.

### 3. `Driver` Interface

The `Driver` interface defines the `navigate` behavior. Each driver type (e.g., `Robot`, `Human`) implements this interface, providing specific navigation capabilities.

```python
class Driver(ABC):
    @abstractmethod
    def navigate(self, destination):
        pass
```

#### Implementations:
- **Robot**: Autonomous navigation.
- **Human**: Human-driven navigation.

## Example Usage

Below is an example of how to use the `Transport` system with different engines and drivers:

```python
if __name__ == "__main__":
    combustion_engine = CombustionEngine()
    electric_engine = ElectricEngine()
    robot_driver = Robot()
    human_driver = Human()

    # Transport with combustion engine and robot driver
    truck = Transport(robot_driver, combustion_engine)
    truck.deliver("City A", "Goods")

    # Transport with electric engine and human driver
    car = Transport(human_driver, electric_engine)
    car.deliver("City B", "Passengers")
```

## Benefits of Using Composition

- **Flexibility**: Easily switch or add new engine and driver types without modifying the `Transport` class.
- **Extensibility**: New engine and driver types can be added without changing existing classes, adhering to the **Open/Closed Principle**.
- **Reusability**: Separate components like `Engine` and `Driver` can be reused across different parts of the codebase.

## Summary

This project demonstrates the **Composition Design Pattern** to build a transport system with decoupled, modular components. By using interfaces for `Engine` and `Driver`, the system achieves high flexibility, allowing it to adapt to new requirements with minimal code changes.
```
```
