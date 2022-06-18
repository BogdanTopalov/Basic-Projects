def on_sale_discount(order):
    order.price *= 0.5
    return order.price


def twenty_percent_discount(order):
    order.price *= 0.8
    return order.price


class Goods:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy is None:
            return self.price
        return self.discount_strategy(self)

    def __str__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"
