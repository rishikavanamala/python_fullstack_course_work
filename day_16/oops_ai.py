"""
=========================================
PYTHON OOPS - COMPLETE BASIC GUIDE
All OOPS Concepts in One File
=========================================
"""

# =========================================
# 1. CLASS AND OBJECT
# =========================================
print("---- Class & Object ----")

class Student:
    def greet(self):
        print("Hello Student")

s1 = Student()   # Object creation
s1.greet()


# =========================================
# 2. CONSTRUCTOR (__init__)
# =========================================
print("\n---- Constructor ----")

class Person:
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person("Rishika", 21)
p1.display()


# =========================================
# 3. CLASS VARIABLE
# =========================================
print("\n---- Class Variable ----")

class College:
    college_name = "ABC University"   # Class variable

    def __init__(self, student_name):
        self.student_name = student_name

c1 = College("Asha")
print(c1.student_name)
print(College.college_name)


# =========================================
# 4. INHERITANCE
# =========================================
print("\n---- Inheritance ----")

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):   # Inheriting Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


# =========================================
# 5. METHOD OVERRIDING
# =========================================
print("\n---- Method Overriding ----")

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):   # Overriding
        print("Child method")

c = Child()
c.show()


# =========================================
# 6. MULTIPLE INHERITANCE
# =========================================
print("\n---- Multiple Inheritance ----")

class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def talents(self):
        print("Cooking")

class Son(Father, Mother):
    pass

s = Son()
s.skills()
s.talents()


# =========================================
# 7. ENCAPSULATION (PRIVATE VARIABLES)
# =========================================
print("\n---- Encapsulation ----")

class Bank:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

b = Bank(1000)
b.deposit(500)
print("Balance:", b.get_balance())


# =========================================
# 8. POLYMORPHISM
# =========================================
print("\n---- Polymorphism ----")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

for animal in (Cat(), Cow()):
    animal.sound()


# =========================================
# 9. ABSTRACTION (Using ABC Module)
# =========================================
print("\n---- Abstraction ----")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

sq = Square(4)
print("Area:", sq.area())


# =========================================
# 10. super() FUNCTION
# =========================================
print("\n---- super() ----")

class Parent2:
    def __init__(self):
        print("Parent constructor")

class Child2(Parent2):
    def __init__(self):
        super().__init__()
        print("Child constructor")

c2 = Child2()


# =========================================
# 11. __str__ METHOD
# =========================================
print("\n---- __str__ Method ----")

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Title: {self.title}"

b1 = Book("Python Basics")
print(b1)


# =========================================
# 12. STATIC METHOD
# =========================================
print("\n---- Static Method ----")

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))


# =========================================
# 13. CLASS METHOD
# =========================================
print("\n---- Class Method ----")

class Company:
    company_name = "Tech Corp"

    @classmethod
    def change_name(cls, new_name):
        cls.company_name = new_name

Company.change_name("New Tech Corp")
print(Company.company_name)


print("\n---- END OF OOPS FILE ----")
