Here's a README file that describes your project in terms of the SOLID principles:

---

# Order Shipping Project

This project demonstrates the use of the **Strategy** design pattern and adheres to several **SOLID principles** to create a flexible, maintainable structure for calculating shipping costs in an order management system. 

## Project Overview

The Order Shipping project allows for calculating shipping costs and delivery dates based on different shipping strategies (e.g., Ground, Air). Instead of hardcoding each shipping method within the `Order` class, we use a **strategy interface** and individual classes for each shipping method. This approach makes the project more modular, maintainable, and open to future expansion.

## SOLID Principles Used

This project exemplifies the SOLID principles in the following ways:

### 1. **Single Responsibility Principle (SRP)**

Each class in the project has a single responsibility:

- **`Order` Class**: Responsible only for holding order details, such as items and weights, and delegating the calculation of shipping costs.
- **`Shipping` Interface**: Defines the basic contract for calculating shipping cost and delivery date, which all shipping methods must follow.
- **`GroundShipping` and `AirShipping` Classes**: Each class is solely responsible for implementing the cost and date calculations for its specific shipping method.

By separating these responsibilities, each class has one reason to change, and we avoid adding complexity to a single class.

### 2. **Open/Closed Principle (OCP)**

The project is open for extension but closed for modification. 

- If we want to add a new shipping method (e.g., `SeaShipping`), we can create a new class that implements the `Shipping` interface without modifying the existing `Order` or other shipping classes. 
- The `Order` class does not need to know the details of any specific shipping method; it only relies on the `Shipping` interface, making the system adaptable to new shipping strategies.

### 3. **Liskov Substitution Principle (LSP)**

The `Order` class works with any subclass of `Shipping` via the `Shipping` interface. 

- Any new `Shipping` subclass (e.g., `GroundShipping`, `AirShipping`) can replace another in the `Order` class without altering functionality. This is because all subclasses implement the same methods (`get_cost` and `get_date`) defined in the `Shipping` interface.
- The `Order` class can substitute one `Shipping` method for another without knowing or caring about the implementation details.

### 4. **Interface Segregation Principle (ISP)**

The `Shipping` interface defines only the methods that are relevant to all types of shipping. 

- It includes `get_cost` and `get_date`, which all shipping methods are expected to implement. 
- This interface keeps each shipping method focused on its core responsibilities and avoids bloating with unnecessary methods. Each shipping class only implements what it needs to fulfill the `Shipping` interface requirements.

### 5. **Dependency Inversion Principle (DIP)**

The `Order` class depends on the `Shipping` abstraction rather than concrete shipping implementations.

- Instead of directly depending on specific classes like `GroundShipping` or `AirShipping`, the `Order` class is designed to work with any class that implements the `Shipping` interface. This abstraction allows the `Order` class to interact with a general shipping interface, making it independent of concrete implementations.
- This decouples the `Order` class from specific shipping methods, allowing flexibility in choosing or extending shipping strategies without changing the core `Order` class.

## Project Structure

```plaintext
order_shipping/
├── __init__.py               
├── main.py                     # Entry point of the application
├── order/
│   ├── __init__.py
│   └── order.py                # Defines the Order class
└── shipping_strategy/
    ├── __init__.py
    ├── ground_shipping.py      # Defines the GroundShipping class
    ├── air_shipping.py         # Defines the AirShipping class
    └── shipping.py             # Defines the Shipping interface
```

## How to Run

1. Navigate to the root directory (`design-patterns`) and run the main script as a module:
   ```bash
   python -m order_shipping.main
   ```

2. This will create an order and calculate the shipping cost using the selected shipping strategy.

## Example Usage

Here’s a basic example of how the project works:

1. Define an `Order` and choose a shipping strategy (e.g., `GroundShipping` or `AirShipping`).
2. Pass the chosen shipping strategy to the `Order`.
3. Calculate the shipping cost and date using the selected strategy.

This allows you to add new shipping strategies without modifying the `Order` class.

## Benefits of This Design

- **Extensibility**: New shipping methods can be added without modifying existing classes.
- **Maintainability**: Each class has a single responsibility, making the code easier to test and maintain.
- **Flexibility**: The `Order` class works with any shipping strategy, making the system more adaptable to changes.

---

This README highlights the SOLID principles implemented in the project, helping to ensure that the code is clean, extensible, and easy to maintain.