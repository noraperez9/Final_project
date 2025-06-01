class Cart:
    def __init__(self):
        self.items = {}  # product name → quantity

    def add_item(self, name):
        # Adds 1 of the given product to the cart
        if name in self.items:
            self.items[name] += 1
        else:
            self.items[name] = 1

    def get_total(self, inventory):
        # Calculates total price
        total = 0
        for name in self.items:
            quantity = self.items[name]
            price = inventory[name].price
            total += price * quantity
        return total

    def get_receipt_lines(self, inventory):
        # Builds receipt lines as strings
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

