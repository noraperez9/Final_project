# product.py
# Author: Samantha Lin and Nora Perez 

class Product:
    # Represents a product in the store with a name, price, and category.

    def __init__(self, name: str, price: float, category: str):
        # Initializes a Product object.
        # name (str): The name of the product
        # price (float): The price of the product
        # category (str): The category the product belongs to (e.g., Dairy, Snacks)
        self.name = name
        self.price = price
        self.category = category
