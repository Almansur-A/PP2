# 1️⃣ Override method
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


# 2️⃣ Override with extension
class Dog(Animal):
    def speak(self):
        print("Woof")

d = Dog()
d.speak()


# 3️⃣ Polymorphism example
animals = [Cat(), Dog()]
for animal in animals:
    animal.speak()


# 4️⃣ Override constructor
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

s = Student("Mike")
print(s.name)


# 5️⃣ Real-world override
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

sq = Square(4)
print(sq.area())
