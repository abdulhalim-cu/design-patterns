from transport import Transport
from combustion_engine import CombustionEngine
from electric_engine import ElectricEngine
from human import Human
from robot import Robot


combustion_engine = CombustionEngine()
electric_engine = ElectricEngine()
human_driver = Human()
robot_driver = Robot()

truck = Transport(human_driver, combustion_engine)
truck.deliver("New York", "Electronics")
autonomous_vehicle = Transport(robot_driver, electric_engine)
autonomous_vehicle.deliver("San Francisco", "Medical Supplies")
