import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_order_initialization(self):
        customer = Customer("Andrew")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0

    def test_price_validation(self):
        customer = Customer("Collins")
        coffee = Coffee("Mocha")
        with pytest.raises(TypeError):
            Order(customer, coffee, "5")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
        with pytest.raises(ValueError):
            Order(customer, coffee, 15.0)
        order = Order(customer, coffee, 5.0)
        with pytest.raises(AttributeError):
            order.price = 6.0

    def test_relationships(self):
        customer = Customer("Santos")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 3.5)
        assert order in customer.orders()
        assert order in coffee.orders()
        assert customer in coffee.customers()
        assert coffee in customer.coffees()