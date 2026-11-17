"""An e-commerce company organizes products using multiple levels. Create classes 
Product → ElectronicProduct → MobilePhone using multilevel inheritance and 
display product details. """

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, warranty, ram):
        super().__init__(name, price, warranty)
        self.ram = ram

    def display(self):
        print(f"{self.name} | Price: {self.price} | Warranty: {self.warranty} yr | RAM: {self.ram}GB")

MobilePhone("Galaxy S", 60000, 2, 8).display()
