from order.order import Order
from shipping_strategy.ground_shipping import GroundShipping
from shipping_strategy.air_shipping import AirShipping

def main():
    ground_shipping = GroundShipping()
    air_shipping = AirShipping()

    order1 = Order(total=120, weight=10, shipping=ground_shipping)
    print("Order 1 - Ground Shipping:")
    print("Cost:", order1.get_shipping_cost())
    print("Delivery Date:", order1.get_shipping_date())
    print()

    order2 = Order(total=80, weight=5, shipping=air_shipping)
    print("Order 2 - Air Shipping:")
    print("Cost:", order2.get_shipping_cost())
    print("Delivery Date:", order2.get_shipping_date())

if __name__ == "__main__":
    main()
