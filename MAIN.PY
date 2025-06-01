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

#Placeholder for main menu logic
#To be completed
#This is the driver file for running the program
