from abc import ABC, abstractmethod

# Encapsulation example
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}"

# Inheritance and Polymorphism example
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Abstraction example
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"

# Method Overriding example
class Parent:
    def show(self):
        return "Parent class"

class Child(Parent):
    def show(self):
        return "Child class"

# Method Overloading (using default arguments) example
class Math:
    def add(self, a, b, c=0):
        return a + b + c

# Main function to demonstrate all concepts
def main():
    # Encapsulation
    person1 = Person("Alice", 30)
    print(person1.get_details())
    
    # Inheritance and Polymorphism
    animals = [Dog("Buddy"), Cat("Whiskers")]
    for animal in animals:
        print(f"{animal.name} says: {animal.speak()}")

    # Abstraction
    vehicles = [Car(), Bike()]
    for vehicle in vehicles:
        print(vehicle.start_engine())

    # Method Overriding
    parent = Parent()
    child = Child()
    print(parent.show())
    print(child.show())

    # Method Overloading
    math = Math()
    print(math.add(1, 2))    # Output: 3
    print(math.add(1, 2, 3)) # Output: 6

if __name__ == "__main__":
    main()
