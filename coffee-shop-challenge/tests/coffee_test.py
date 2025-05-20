import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def test_coffee_initialization(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"

    def test_name_validation(self):
        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("A")
        coffee = Coffee("Mocha")
        with pytest.raises(AttributeError):
            coffee.name = "New Name"

    def test_orders_relationship(self):
        coffee = Coffee("Espresso")
        customer = Customer("Zain")
        order = Order(customer, coffee, 3.0)
        assert len(coffee.orders()) == 1
        assert order in coffee.orders()

    def test_customers_relationship(self):
        coffee = Coffee("Cappuccino")
        customer1 = Customer("Erick")
        customer2 = Customer("Frank")
        Order(customer1, coffee, 4.0)
        Order(customer1, coffee, 4.5)
        Order(customer2, coffee, 3.5)
        assert len(coffee.customers()) == 2
        assert customer1 in coffee.customers()
        assert customer2 in coffee.customers()

    def test_num_orders(self):
        coffee = Coffee("Americano")
        assert coffee.num_orders() == 0
        Order(Customer("Stella"), coffee, 2.5)
        Order(Customer("Henry"), coffee, 3.0)
        assert coffee.num_orders() == 2

    def test_average_price(self):
        coffee = Coffee("Flat White")
        assert coffee.average_price() == 0
        Order(Customer("Ian"), coffee, 4.0)
        Order(Customer("Mohammed"), coffee, 6.0)
        assert coffee.average_price() == 5.0