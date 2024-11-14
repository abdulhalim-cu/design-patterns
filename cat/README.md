# Cat Folder

This folder contains the implementation of a simple simulation involving a `Cat` and its interactions with different types of `Food`. The code is organized into separate files for better modularity, reusability, maintainability, and testing.

## Overview

The main components of this project are:
- `Cat` class: Represents a cat with attributes such as energy.
- `Food` class: Represents food items that the cat can consume.
- `Sausage` class: A specific type of food.
- `Fish` class: Another specific type of food.

## Benefits of Separate Files

- **Modularity**: Each class is contained in its own file, making the code more organized.
- **Reusability**: You can reuse `Food`, `Sausage`, `Fish`, and `Cat` classes in other projects without having to copy-paste large chunks of code.
- **Maintainability**: When you want to modify a class, you only need to update one file.
- **Testing**: You can test each class independently by importing only the file you need in a test script.

## Example Usage

Here is an example of how the classes might be used together:

```python
from cat import Cat
from food import Food, Sausage, Fish

# Create instances of food
sausage = Sausage()
fish = Fish()

# Create an instance of a cat
cat = Cat()

# Feed the cat
cat.eat(sausage)
cat.eat(fish)

# Print the cat's total energy
print(f"Cat's total energy: {cat.energy}")  # Output: Cat's total energy: 250
```

## Classes
### Cat
The Cat class represents a cat with attributes such as energy. It has methods to eat food and increase its energy.

### Food
The Food class is a base class for different types of food. It has attributes such as energy value.

### Sausage
The Sausage class is a subclass of Food and represents a specific type of food with its own energy value.

### Fish
The Fish class is a subclass of Food and represents another specific type of food with its own energy value.

## Conclusion
This project demonstrates the benefits of organizing code into separate files for better modularity, reusability, maintainability, and testing. Each class can be independently developed and tested, making the overall project more manageable.