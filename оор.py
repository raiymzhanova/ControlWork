# 1Инкапсуляция
class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self._age = age
        print(f"Возраст успешно установлен на {self._age}")
    def get_age(self):
        return self._age

# Пример использования

p = Person()

print("Устанавливаем возраст на 25")
p.set_age(25)

print(f"Текущий возраст: {p.get_age()}")

print(f"Пытаемся устаносить возраст (-5)....")
try:
    p.set_age(-5)

except ValueError as e:
 print(f"ОШИБКА!: {e}")

 print(f"Возраст после неудачной попытки: {p.get_age()}")


# 2Наследование
class Animal:

   def __init__(self, name):
        self.name = name

   def speak(self):
      return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# пример использования
Dog = Dog("Buddy")
Cat = Cat("Kitty")

print(f"Dog: {Dog.name}, says : {Dog.speak()}")
print(f"Cat: {Cat.name}, says: {Cat.speak()}")



# полиморфизм
class Vehicle:

    def move(self):

        return "Vehicle is moving"

class Car(Vehicle):

    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):

    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
        return vehicle.move()

# Пример использования
car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))




# 4Абстракция
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
         pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):

        return math.pi * self.radius ** 2

# Пример использования
rect = Rectangle(25, 550)
circle = Circle( 38)

print(f"Площадь прямоугольника: {rect.area()}")
print(f"Площадь круга: {circle.area():.2f}")
