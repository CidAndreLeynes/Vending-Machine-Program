from typing import NamedTuple

class Product(NamedTuple):
    name: str
    price: int
    id: int

PRODUCTS = [
    Product("Mineral Water", 100, 12),
    Product("Wonda Coffee", 200, 13),
    Product("Chocolate Milk", 200, 14),
    Product("Coke", 200, 15),
    Product("Kitkat", 300, 16),
    Product("Redbull", 300, 17),
    Product("Snickers", 400, 18),
    Product("Chocolate_Bun", 500, 19),
    Product("CookiesCream", 500, 20),
]

MONEY_UNITS = [
    ('RM100', 10_000),
    ('RM50', 5_000),
    ('RM20', 2_000),
    ('RM10', 1_000),
    ('RM5', 500),
    ('RM1', 100),
    ('quarters', 25),
    ('dimes', 10),
    ('pennies', 1),
]

MAX_NAME_LENGTH = max(len(prod.name) for prod in PRODUCTS)
MAX_PRICE_LENGTH = max(len(str(prod.price)) for prod in PRODUCTS)
MAX_ID_LENGTH = max(len(str(prod.id)) for prod in PRODUCTS)

print("Welcome to Chris's vending machine\n")
print("Product Price Code")

for product in PRODUCTS:
    print(
        f"{product.name:<{MAX_NAME_LENGTH}} "
        f"RM{product.price//100:<{MAX_PRICE_LENGTH-2}} "
        f"{product.id:<{MAX_ID_LENGTH}}"
    )

product_id = int(input("Type a product code to continue..."))

for product in PRODUCTS:
    if product.id == product_id:
        print(f"You have selected {product.name}. Pay RM{product.price}")
        break
else:
    print("Error: No such product")

# Not sure why you're ignoring the original price of the product/asking the user to give it
# cost = int(input('Cost: ')) * 100
amount_paid = int(input("Amount paid: ")) * 100
change_breakdown = {}
change = amount_paid - product.price

if change < 0:
    print("Error: InsufficientFunds")

for name, value in MONEY_UNITS:
    amount, change = divmod(change, value)
    change_breakdown[name] = amount
 
print(change_breakdown)