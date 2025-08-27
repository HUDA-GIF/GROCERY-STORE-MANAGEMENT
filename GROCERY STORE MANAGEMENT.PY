# Grocery Store Management System
# No external libraries used

import os

# Inventory stored as dictionary {item: [price, quantity]}
inventory = {
    "Apples": [3, 50],
    "Bananas": [1, 100],
    "Rice": [2, 80],
    "Milk": [4, 30]
}

def display_inventory():
    print("\n--- Grocery Store Inventory ---")
    print("{:<15} {:<10} {:<10}".format("Item", "Price($)", "Quantity"))
    for item, details in inventory.items():
        print("{:<15} {:<10} {:<10}".format(item, details[0], details[1]))
    print("-" * 40)

def add_item():
    item = input("Enter item name: ").capitalize()
    if item in inventory:
        print("Item already exists. Updating quantity instead.")
        inventory[item][1] += int(input("Enter quantity to add: "))
    else:
        price = int(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        inventory[item] = [price, qty]
    print(f"{item} added/updated successfully!")

def update_item():
    item = input("Enter item name to update: ").capitalize()
    if item in inventory:
        price = int(input("Enter new price: "))
        qty = int(input("Enter new quantity: "))
        inventory[item] = [price, qty]
        print(f"{item} updated successfully!")
    else:
        print("Item not found in inventory!")

def search_item():
    item = input("Enter item name to search: ").capitalize()
    if item in inventory:
        print(f"{item} found - Price: ${inventory[item][0]}, Quantity: {inventory[item][1]}")
    else:
        print("Item not found!")

def purchase_items():
    bill = 0
    while True:
        item = input("Enter item to purchase (or 'done' to finish): ").capitalize()
        if item.lower() == "done":
            break
        if item in inventory:
            qty = int(input("Enter quantity: "))
            if qty <= inventory[item][1]:
                cost = inventory[item][0] * qty
                bill += cost
                inventory[item][1] -= qty
                print(f"{item} added to bill, cost: ${cost}")
            else:
                print("Not enough stock!")
        else:
            print("Item not available!")
    print(f"\nTotal Bill: ${bill}")

def save_inventory():
    with open("inventory.txt", "w") as f:
        for item, details in inventory.items():
            f.write(f"{item},{details[0]},{details[1]}\n")
    print("Inventory saved successfully!")

def load_inventory():
    global inventory
    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "r") as f:
            inventory = {}
            for line in f:
                item, price, qty = line.strip().split(",")
                inventory[item] = [int(price), int(qty)]

def main():
    load_inventory()
    while True:
        print("\n--- Grocery Store Menu ---")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Search Item")
        print("5. Purchase Items")
        print("6. Save and Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            search_item()
        elif choice == "5":
            purchase_items()
        elif choice == "6":
            save_inventory()
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()