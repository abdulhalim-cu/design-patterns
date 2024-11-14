from cat import Cat
from sausage import Sausage
from fish import Fish


cat = Cat()
sausage = Sausage()
fish = Fish()


cat.eat(sausage)
cat.eat(fish)
cat.eat(sausage)
cat.eat(fish)

print(f"Cat's total energy: {cat.energy}")