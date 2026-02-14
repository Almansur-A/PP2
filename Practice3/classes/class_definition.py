# 1️⃣ Basic class
class Person:
    pass

p = Person()


# 2️⃣ Class with attribute
class Dog:
    species = "Canine"

print(Dog.species)


# 3️⃣ Object creation
class Car:
    def drive(self):
        print("Driving")

c = Car()
c.drive()


# 4️⃣ Multiple objects
c2 = Car()
c2.drive()


# 5️⃣ Class docstring
class Book:
    """Represents a book."""
    pass
