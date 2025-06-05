# test_cart.py
# Author: Samantha Lin and Nora Perez

import unittest
from CART import Cart
from PRODUCT import Product


class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.inventory = {
            "Milk": Product("Milk", 3.00, "Dairy"),
            "Bread": Product("Bread", 2.50, "Bakery")
        }

    def test_add_item_once(self):
        self.cart.add_item("Milk")
        self.assertEqual(self.cart.items["Milk"], 1)

    def test_add_item_twice(self):
        self.cart.add_item("Milk")
        self.cart.add_item("Milk")
        self.assertEqual(self.cart.items["Milk"], 2)

    def test_get_total_single_item(self):
        self.cart.add_item("Milk")
        total = self.cart.get_total(self.inventory)
        self.assertEqual(total, 3.00)

    def test_get_total_multiple_items(self):
        self.cart.add_item("Milk")
        self.cart.add_item("Bread")
        total = self.cart.get_total(self.inventory)
        self.assertEqual(total, 5.50)

    def test_receipt_lines_format(self):
        self.cart.add_item("Milk")
        lines = self.cart.get_receipt_lines(self.inventory)
        self.assertIn("Milk x1 = $3.0", lines)
        self.assertTrue(lines[-1].startswith("Total ="))


if __name__ == "__main__":
    unittest.main()
