inventory = {
    'apple': 25,
    'banana': 15,
    'orange': 20,
    'grapes': 35,
    'watermelon': 50,
    'patato':30,
    'tamato':30,
    'ps5':50000,
    'pencil':5,
    'erasure':2
}
def display_inventory():
    print("Available items:")
    for item, price in inventory.items():
        print(f"{item.capitalize()}: ₹{price}")


def calculate_bill(cart):
    total = 0
    for item, quantity in cart.items():
        total += inventory[item] * quantity
    return total


def main():
    cart = {}
    while True:
        display_inventory()
        choice = input("Enter the item you want to buy (or 'done' to finish shopping): ").lower()
        if choice == 'd':
            break
        elif choice in inventory:
            quantity = int(input(f"Enter the quantity of {choice}: "))
            cart[choice] = quantity
        else:
            print("Invalid item! Please choose from the available items.")

    print("\nYour cart:")
    for item, quantity in cart.items():
        print(f"{item.capitalize()}: {quantity}")

    total_bill = calculate_bill(cart)
    print(f"\nTotal Bill: ₹{total_bill}")



main()
