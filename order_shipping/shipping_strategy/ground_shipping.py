from shipping_strategy.shipping import Shipping


class GroundShipping(Shipping):
    def get_cost(self, order) -> float:
        if order.get_total() > 100:
            return 0  # Free delivery for orders over $100
        return max(10, order.get_weight() * 1.5)

    def get_date(self, order) -> str:
        return "5-7 business days"