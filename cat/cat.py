from food import Food


class Cat:
    def __init__(self) -> None:
        self.energy = 0

    def eat(self, food: Food) -> None:
        self.energy += food.get_nutrition()
        print(f"Cat ate {food.get_color()} food and gained {food.get_nutrition()} energy.")
