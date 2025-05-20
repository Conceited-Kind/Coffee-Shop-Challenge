import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_initialization(self):
        customer = Customer("Allan")
        assert customer.name == "Allan"

    def test_name_validation(self):
        with pytest.raises(ValueError):
            Customer(123)
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")
        customer = Customer("Allan")
        customer.name = "Bob"
        assert customer.name == "Bob"

    def test_orders_relationship(self):
        customer = Customer("Derrick")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert len(customer.orders()) == 1
        assert order in customer.orders()

    def test_coffees_relationship(self):
        customer = Customer("Tevin")
        coffee1 = Coffee("Mocha")
        coffee2 = Coffee("Espresso")
        Order(customer, coffee1, 4.5)
        Order(customer, coffee1, 5.0)
        Order(customer, coffee2, 3.5)
        assert len(customer.coffees()) == 2
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()

    def test_create_order(self):
        customer = Customer("Tevin")
        coffee = Coffee("Mocha")
        order = customer.create_order(coffee, 4.5)
        assert len(customer.orders()) == 1
        assert order in customer.orders()
        assert order.coffee == coffee
        assert order.price == 4.5

    def test_most_aficionado(self):
        coffee = Coffee("Latte")
        customer1 = Customer("Allan")
        customer2 = Customer("Derrick")
        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 10.0)
        aficionado = Customer.most_aficionado(coffee)
        assert aficionado == customer2
        empty_coffee = Coffee("Espresso")
        assert Customer.most_aficionado(empty_coffee) is None