from engine import Engine
from driver import Driver


class Transport:
    def __init__(self, driver: Driver, engine: Engine):
        self.driver = driver
        self.engine = engine

    def deliver(self, destination, cargo):
        print(f"Starting delivery of {cargo} to {destination}.")
        self.engine.move()
        self.driver.navigate()
        print(f"{cargo} has been delivered to {destination}.\n")
