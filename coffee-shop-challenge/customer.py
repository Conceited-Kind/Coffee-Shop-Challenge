class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order  # Import here
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        from order import Order  # Import here
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order  # Import here
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order  # Import here
        from coffee import Coffee  # Import here
        if not isinstance(coffee, Coffee):
            raise TypeError("Must be a Coffee instance")
        customers_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                customers_spending[order.customer] = customers_spending.get(order.customer, 0) + order.price
        return max(customers_spending.items(), key=lambda x: x[1])[0] if customers_spending else None