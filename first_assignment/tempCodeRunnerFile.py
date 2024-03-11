supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 10},
    "butter": {"qunatity": 12, "price": 100},
    "apples": {"qunatity": 5, "price": 20},
}

customers = ["Ram", "Sita", "Hari"]

shopping_lists = {
    "Ram": [("milk", 4), ("biscuits", 6)],
    "Sita": [("butter", 8), ("apples", 1)],
    "Hari": [("milk", 2)],
}

# Fillings the carts
carts = {}
for customer in customers:
    carts[customer] = []
    for articles in supermarket:
        if articles in supermarket:
            if supermarket[articles]["quantity"] < quantity:
                quantity = supermarket[articles]["quantity"]
            if quantity:
                supermarket[articles]["quantity"] -= quantity
                carts[customer], append((articles, quantity))

for customer in customers:
    print(carts[customer])

print("Checkout")
for customet in customers:
    print("\n Checkout for " + customer + ":")
    total_sum = 0

    for name, quantity in carts[customer]:
        unit_price = supermarket[name]["price"]
        item_sum = quantity * unit_price
        print(f"{quantity:3d} {name:20s} {unit_price:8.2f} {item_sum:8.2f}")
        total_sum += item_sum
    print(f"Total sum: {total_sum:11.2f}")
