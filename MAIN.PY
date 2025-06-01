class Cart:
    def __init__(self):
        self.items = {}  # product name → quantity
    #Initializes an empty shopping cart
    #Item: product name(str), quantity(int)

    def add_item(self, name):
        # Adds 1 of the given product to the cart
        #Parameters: Name(srt): the name of product to add
        #Returns - none
        if name in self.items:
            self.items[name] += 1
        else:
            self.items[name] = 1

    def get_total(self, inventory):
        # Calculates total price
        #Parameter: inventory(dict): product name(str) -> product object
        #Returns: Float, total price of the cart
        total = 0
        for name in self.items:
            quantity = self.items[name]
            price = inventory[name].price
            total += price * quantity
        return total

    def get_receipt_lines(self, inventory):
        # Creates a list of strings representing the receipt
        #Parameters: Inventory(dict): Product name(str) -> Product object
        #Returns: list of str representing the receipt lines
        lines = []
        total = 0
        for name in self.items:
            quantity = self.items[name]
            price = inventory[name].price
            subtotal = price * quantity
            total += subtotal
            lines.append(name + " x" + str(quantity) + " = $" + str(subtotal))
        lines.append("Total = $" + str(total))
        return lines

