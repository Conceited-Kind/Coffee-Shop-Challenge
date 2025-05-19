from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("=== COFFEE SHOP ===\n")
    Order.all = []  
    # Create customers
    print("Creating customers...")
    alice = Customer("Allan")
    bob = Customer("Derrick")

    # Create coffees
    print("Creating coffees...")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    # Place orders
    print("\nPlacing orders...")
    order1 = Order(alice, latte, 5.0)
    order2 = Order(bob, espresso, 3.5)
    order3 = Order(alice, espresso, 4.0)

    # Check relationships
    print("\nTesting relationships:")
    print(f"{alice.name}'s orders:", [o.coffee.name for o in alice.orders()])
    print(f"{bob.name}'s coffees:", [c.name for c in bob.coffees()])
    print(f"{latte.name} customers:", [c.name for c in latte.customers()])

    # Check totals and averages
    print("\nTesting aggregates:")
    print(f"Total {espresso.name} orders:", espresso.num_orders())
    print(f"Avg {espresso.name} price:", espresso.average_price())

    # Check most aficionado
    print("\nTesting most_aficionado:")
    aficionado = Customer.most_aficionado(espresso)
    print(f"Most aficionado for {espresso.name}: {aficionado.name if aficionado else None}")

if __name__ == "__main__":
    main()