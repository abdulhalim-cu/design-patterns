from shipping_strategy.shipping import Shipping

class Order:
    def __init__(self, total, weight, shipping: Shipping):
        self.total = total
        self.weight = weight
        self.shipping = shipping

    def get_total(self):
        return self.total

    def get_weight(self):
        return self.weight

    def get_shipping_cost(self):
        return self.shipping.get_cost(self)
    
    def get_shipping_date(self):
        return self.shipping.get_date(self)