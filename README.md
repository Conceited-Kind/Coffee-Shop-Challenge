# Coffee Shop Challenge

This project simulates a simple coffee shop system using Python classes. It demonstrates object-oriented programming concepts such as relationships between customers, coffees, and orders, as well as basic data aggregation.

## Project Structure

```
coffee-shop-challenge/
├── coffee.py
├── customer.py
├── order.py
├── debug.py
└── tests/
    ├── coffee_test.py
    ├── customer_test.py
    └── order_test.py
```

## Main Components

- **Customer**: Represents a customer in the coffee shop.
- **Coffee**: Represents a type of coffee.
- **Order**: Represents an order placed by a customer for a coffee.

## How to Run

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies** (if any) using pipenv or pip.

3. **Run the debug script** to see the relationships and aggregates in action:

   ```sh
   cd /home/allan/Phase3/Coffee-Shop-Challenge
   python -m coffee-shop-challenge.debug
   ```

   This will print out sample customers, coffees, orders, and some aggregate statistics.

## Running Tests

Tests are located in the `tests/` directory and use `pytest`. To run the tests:

```sh
cd /home/allan/Phase3/Coffee-Shop-Challenge
pipenv run pytest coffee-shop-challenge/tests/
python debug.py
```

## Notes

- The code uses relative imports, so run scripts as modules from the project root.
- The `debug.py` script demonstrates the main features and relationships.

## License

This project is for educational purposes.