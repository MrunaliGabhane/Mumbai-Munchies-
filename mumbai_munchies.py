class Snack:
    def __init__(self, id, name, price, available):
        self.id = id
        self.name = name
        self.price = price
        self.available = available

# Create an empty list to store the snacks inventory
snacks_inventory = []

def add_snack():
    # Prompt the user for snack details
    id = input("Enter snack ID: ")
    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    available = input("Is the snack available? (yes/no): ")

    # Create a new snack instance
    snack = Snack(id, name, price, available)

    # Add the snack to the inventory
    snacks_inventory.append(snack)

    print("Snack added to inventory successfully!")

def remove_snack():
    id = input("Enter snack ID to remove: ")

    # Find the snack in the inventory
    for snack in snacks_inventory:
        if snack.id == id:
            snacks_inventory.remove(snack)
            print("Snack removed from inventory successfully!")
            return

    print("Snack not found in the inventory.")

def update_availability():
    id = input("Enter snack ID to update availability: ")
    available = input("Is the snack available? (yes/no): ")

    # Find the snack in the inventory
    for snack in snacks_inventory:
        if snack.id == id:
            snack.available = available
            print("Snack availability updated successfully!")
            return

    print("Snack not found in the inventory.")

def record_sale():
    id = input("Enter snack ID sold: ")

    # Find the snack in the inventory
    for snack in snacks_inventory:
        if snack.id == id:
            if snack.available == "yes":
                snack.available = "no"
                print("Sale recorded successfully!")
                return
            else:
                print("Snack is not available for sale.")
                return

    print("Snack not found in the inventory.")

# Main loop to interact with the canteen staff
while True:
    print("\nMenu:")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update snack availability")
    print("4. Record a sale")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        record_sale()
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")