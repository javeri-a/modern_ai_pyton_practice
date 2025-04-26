 
# ___________________________DAY 01 OOP__________________________________________

#____________________________THEORY OOP__________________________________________

# Day 1: Introduction to Object-Oriented Programming (OOP)
# What is OOP?
# Imagine you're building a game. You need to create characters, weapons, enemies, and scores, right? Each of these things (characters, weapons, etc.) can be thought of as objects.

# OOP helps you create these objects and define how they should behave and interact with each other. OOP is like organizing your entire game into little pieces, making it manageable, reusable, and easy to scale.

# 4 Main Principles of OOP:
# Encapsulation: Hiding the internal details of an object and only exposing what's necessary. (Think of a vending machine – you don’t need to know how it works, just insert coins and get the snack!)

# Inheritance: Reusing code from one class (parent) in another (child class). For example, a Dog class can inherit from a Pet class (a dog is a type of pet).

# Polymorphism: The ability of different objects to respond to the same method in their own way. It’s like sending a message to different characters in a game, and they all react differently!

# Abstraction: Hiding the complex details and only showing the essentials. Like using a remote control without needing to know how the TV works internally.


# ______________________________PRACTICAL________________________________________
class  car:
    def __init__(self,maker,model, brand,year):
        self.maker = maker
        self.model = model
        self.brand = brand
        self.year = year

    def details_of_car(self):
        print(f"THIS A NAME OF CAR MAKER {self.maker} AND MODEL IS {self.model}. OUR BRAND IS {self.brand} AND THE CAR IS MAKE IN {self.year},  its a detail i hope you are buy")

    def not_satisfy(self):
         print(f"THIS A NAME OF CAR MAKER __ {self.maker} AND MODEL IS __{self.brand} AND THE CAR IS MAKE IN  {self.year}, I will try to contact you again....")
 
car1 =  car("Ali", "corola","TOYOTA",2022)
car1.details_of_car()
car1.not_satisfy()
    
 
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greet(self):
        print(f"Hello, my name is {self.name}.")

person1 = Person("Javeria", 20, "Karachi")
person1.greet()


class Student:
 def __init__(self,name,age,rollnumber,slot,quarter):
     self.name = name
     self.age = age
     self.rollnumber = rollnumber
     self.slot = slot
     self.quarter = quarter

 def student_details(self):
    print(f"SHE IS A {self.name}, AGE IS {self.age} YEAR OLD. ROLL NUMBER IS {self.rollnumber}, SLOT IS {self.slot}. AND THE QUARTER IS { self.quarter}.")
     
student1 = Student("JIYA",20,65511,"FRIDAY, 9AM TO 12PM" , 3 )
student1.student_details()



class Furniture:
    def __init__(self,name,warranty,price):
        self.name = name
        self.warranty = warranty
        self.price = price

    def detail(self):
        print(f"our furniture name is {self.name} it have {self.warranty} months.and its price {self.price}$")

detailsFur = Furniture("Bed",12, 279)
detailsFur.detail()

class Furniture:
    def __init__(self,name,warranty,price):
        self.name = name
        self.warranty = warranty
        self.price = price

    def detail(self):
        print(f"our furniture name is {self.name} it have {self.warranty} months.and its price {self.price}$")

detailsFur = Furniture("Bed",12, 279)
detailsFur.detail()

