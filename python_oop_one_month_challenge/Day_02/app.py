
#_________________________________________DAY 02_____________________________________________
# _________________________________RECAP DAY 01_________________________________
class car:
    def __init__ (self,name,brand,year):
        self.name = name
        self.brand = brand
        self.year = year

    def start_engine(self):
        print(f"{self.name} and {self.brand} engine started...")

    def stop_engine(self):
        print(f"{self.name}, {self.brand} and {self.year} engine stoped...")   

car1 = car("civic","toyota",2023)
car1.start_engine()
car1.stop_engine()


#_____________________________________THEORY OF DAY 02__________________________________________
# (1) Inheritance
# (2) Polymorphism
# (3) Encapsulation

# 1. Inheritance (Roman Urdu)
# Meaning:
# Ek class apni properties aur methods dusri class ko de sakti hai — is process ko inheritance kehte hain.
# Jaise mummy ki kuch cheezein apko virasat mein milti hain — waise ek "Parent Class" ki cheezein "Child Class" ko milti hain.

# Real Life Example:

# "Car" ek general class hai.

# "SportsCar" ek special car hai jo Car wali properties inherit karti hai aur apni extra property bhi rakhti hai jaise "top speed".


# 2. Polymorphism (Roman Urdu)
# Meaning:
# Ek hi method ka naam same hota hai lekin har class mein alag tareeke se kaam karta hai.
# Jaise ek aadmi ghar mein husband hai, office mein employee hai — role change hota hai, lekin aadmi wahi hai.

# Real Life Example:

# Car ka engine start karna — Electric car silently start karti hai, petrol car awaaz ke saath.

# 3. Encapsulation (Roman Urdu)
# Meaning:
# Apne data ko lock karna — direct access na dena, sirf methods ke zariye control karna.

# Real Life Example:

# Bank account ka balance — direct kisi ko nahi dikhate, sirf transaction karne ka system dete hain.


#_________________________________________01 INHERITANCE_________________________________________________


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.make} {self.model} engine started!")

class SportsCar(Car):
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self.top_speed = top_speed

    def show_speed(self):
        print(f"Top speed is {self.top_speed} km/h")


car1 = Car("Toyota", "Corolla", 2022)
sports_car1 = SportsCar("Ferrari", "488", 2022, 330)

car1.start_engine()
sports_car1.start_engine()
sports_car1.show_speed()




class car:
    def __init__(self,model , year, make):
        self.model = model
        self.year = year
        self.make = make

    def  start_engine(self):
     print(f"{self.model} {self.year} engine started!")

class sportCar(car):
    def __init__(self,model , year, make, speed):
        super().__init__(model , year, make)
        self.speed = speed

    def show_speed (self):
        print(f"Top speed is {self.speed} km/h")

car1 = car("civic",2025,"toyota")
car2 = sportCar("Mercedes",2023,"honda",500)

car1.start_engine()
car2.show_speed ()
car2.start_engine()

