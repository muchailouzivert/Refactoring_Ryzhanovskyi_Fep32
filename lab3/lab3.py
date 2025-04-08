from typing import List, Dict

class User:
    def __init__(self, user_id: int, name: str, email: str, password: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.orders: List[Order] = []

    def register(self):
        return f"User {self.name} registered successfully."
    
    def login(self):
        return f"User {self.name} has logged in."
    
    def view_orders(self):
        return self.orders

class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity: int):
        if self.stock + quantity >= 0:
            self.stock += quantity
        else:
            print("Not enough stock available.")

class Order:
    def __init__(self, order_id: int, user: User):
        self.id = order_id
        self.user = user
        self.products: List[Product] = []
        self.total_price = 0.0
    
    def add_product(self, product: Product):
        self.products.append(product)
        self.total_price += product.price
    
    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
            self.total_price -= product.price
    
    def calculate_total(self):
        return sum(product.price for product in self.products)

class ShoppingCart:
    def __init__(self, user: User):
        self.user = user
        self.items: Dict[Product, int] = {}
    
    def add_item(self, product: Product, quantity: int):
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            product.update_stock(-quantity)
        else:
            print("Not enough stock available.")
    
    def remove_item(self, product: Product):
        if product in self.items:
            product.update_stock(self.items[product])
            del self.items[product]
    
    def clean_cart(self):
        for product, quantity in self.items.items():
            product.update_stock(quantity)
        self.items.clear()
    
    def checkout(self) -> Order:
        order = Order(order_id=len(self.user.orders) + 1, user=self.user)
        for product, quantity in self.items.items():
            for _ in range(quantity):
                order.add_product(product)
        self.user.orders.append(order)
        self.items.clear()
        return order