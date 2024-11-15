from shipping_strategy.shipping import Shipping

class AirShipping(Shipping):
    def get_cost(self, order) -> float:
        return max(20, order.get_weight() * 3)

    def get_date(self, order) -> str:
        return "2-3 business days"
