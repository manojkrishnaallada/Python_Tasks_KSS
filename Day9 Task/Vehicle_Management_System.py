"""A transport company manages different vehicles. Create a base class Vehicle with 
attributes like brand and speed. Create derived classes Car and Bike that inherit from 
Vehicle and display their details."""

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def display(self):
        print(f"Car -> Brand: {self.brand}, Speed: {self.speed} km/h")

class Bike(Vehicle):
    def display(self):
        print(f"Bike -> Brand: {self.brand}, Speed: {self.speed} km/h")

Car("Toyota", 180).display()
Bike("Yamaha", 120).display()
