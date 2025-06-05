
from product import Product
from cart import Cart

def display_menu():
    print("\n--- Grocery Store Menu ---")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. Checkout and Exit")

def display_products(inventory):
    print("\nAvailable Products:")
    for name, product in inventory.items():
        price = str(product.price)  # convert price to string
        category = product.category
        print(name + " - $" + price + " (" + category + ")")

def main():
    # Inventory of products
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
        "Cookies": Product("Cookies", 2.20, "Snacks"),
        "Chocolate": Product("Chocolate", 1.80, "Snacks"),
        "Nuts": Product("Nuts", 3.50, "Snacks"),
    }

    cart = Cart()

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_products(inventory)

        elif choice == "2":
            product_name = input("Enter product name to add: ").strip()
            if product_name in inventory:
                cart.add_item(product_name)
                print(f"{product_name} added to cart.")
            else:
                print("Product not found.")

        elif choice == "3":
            print("\n--- Receipt ---")
            receipt_lines = cart.get_receipt_lines(inventory)
            for line in receipt_lines:
                print(line)
            with open("receipt.txt", "w") as file:
                for line in receipt_lines:
                    file.write(line + "\n")
            print("Receipt saved to receipt.txt. Thank you!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
