#main.py
#Author: Samantha Lin and Nora Perez
from PRODUCT import Product
from CART import Cart

# Inventory: All available products
inventory = {
    "Milk": Product("Milk", 3.00, "Dairy"),
    "Cheese": Product("Cheese", 4.50, "Dairy"),
    "Yogurt": Product("Yogurt", 1.20, "Dairy"),
    "Butter": Product("Butter", 2.80, "Dairy"),

    "Apples": Product("Apples", 0.99, "Fruit"),
    "Bananas": Product("Bananas", 0.50, "Fruit"),
    "Oranges": Product("Oranges", 1.10, "Fruit"),
    "Strawberries": Product("Strawberries", 3.00, "Fruit"),

    "Bread": Product("Bread", 2.50, "Bakery"),
    "Bagels": Product("Bagels", 2.80, "Bakery"),
    "Croissant": Product("Croissant", 1.50, "Bakery"),
    "Donut": Product("Donut", 1.20, "Bakery"),

    "Water": Product("Water", 1.00, "Beverages"),
    "Soda": Product("Soda", 1.30, "Beverages"),
    "Juice": Product("Juice", 2.00, "Beverages"),
    "Coffee": Product("Coffee", 4.00, "Beverages"),

    "Chips": Product("Chips", 1.70, "Snacks"),
    "Cookies": Product("Cookies", 2.20, "Snacks"),
    "Chocolate": Product("Chocolate", 1.80, "Snacks"),
    "Nuts": Product("Nuts", 3.50, "Snacks")
}

# Initialize cart
cart = Cart()

def display_products():
    # Displays all available products with their prices and categories.
    print("\nAvailable Products:")
    for name, product in inventory.items():
        print(f"{name} - ${product.price:.2f} ({product.category})")

def main():
    # Main loop for running the grocery store program.
    print("Welcome to the Grocery Store!")

    while True:
        print("\nMenu:")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. Checkout and Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            display_products()

        elif choice == "2":
            product_name = input("Enter the product name to add: ").strip()
            if product_name in inventory:
                cart.add_item(product_name)
                print(f"{product_name} added to cart.")
            else:
                print("Product not found. Try again.")

        elif choice == "3":
            print("\nYour Receipt:")
            receipt_lines = cart.get_receipt_lines(inventory)
            for line in receipt_lines:
                print(line)

            with open("receipt.txt", "w") as file:
                for line in receipt_lines:
                    file.write(line + "\n")
            print("Receipt saved to 'receipt.txt'.")
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
