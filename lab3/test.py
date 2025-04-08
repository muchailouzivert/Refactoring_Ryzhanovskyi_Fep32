import unittest
from lab3 import User, Product, ShoppingCart, Order

class ShopTest(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "John Duck", "john@gmail.com", "password")
        self.product1 = Product(1, "Gaming Pc", 1000.0, 10)
        self.product2 = Product(2, "Laptop", 500.0, 5)
        self.cart = ShoppingCart(self.user)
        self.order = Order(1, self.user)

    def test_user_registration(self):
        self.assertEqual(self.user.register(), "User John Duck registered successfully.")
    
    def test_user_login(self):
        self.assertEqual(self.user.login(), "User John Duck has logged in.")
    
    def test_add_product_to_cart(self):
        self.cart.add_item(self.product1, 2)
        self.assertEqual(self.cart.items[self.product1], 2)
    
    def test_remove_product_from_cart(self):
        self.cart.add_item(self.product1, 2)
        self.cart.remove_item(self.product1)
        self.assertNotIn(self.product1, self.cart.items)
    
    def test_clean_cart(self):
        self.cart.add_item(self.product1, 2)
        self.cart.clean_cart()
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.product1.stock, 10)
    
    def test_checkout_creates_order(self):
        self.cart.add_item(self.product1, 1)
        order = self.cart.checkout()
        self.assertEqual(len(self.user.orders), 1)
        self.assertEqual(order.total_price, 1000.0)
    
    def test_order_add_product(self):
        self.order.add_product(self.product1)
        self.assertIn(self.product1, self.order.products)
    
    def test_order_remove_product(self):
        self.order.add_product(self.product1)
        self.order.remove_product(self.product1)
        self.assertNotIn(self.product1, self.order.products)
    
    def test_order_total_price(self):
        self.order.add_product(self.product1)
        self.order.add_product(self.product2)
        self.assertEqual(self.order.calculate_total(), 1500.0)
    
    def test_product_stock_update(self):
        self.product1.update_stock(-3)
        self.assertEqual(self.product1.stock, 7)


    def test_user_order(self):
        self.cart.add_item(self.product1, 1)
        self.cart.add_item(self.product2, 2)
        self.assertTrue(self.product1.stock >= 1)
        self.assertTrue(self.product2.stock >= 2)  
        order = self.cart.checkout()
        self.assertEqual(len(self.user.orders), 1)
        self.assertIn(self.product1, order.products)
        self.assertIn(self.product2, order.products)
        self.assertEqual(order.calculate_total(), 2000.0)


if __name__ == "__main__":
    unittest.main()