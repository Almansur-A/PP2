# 1️⃣ Basic inheritance
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


# 2️⃣ Access parent method
class Cat(Animal):
    pass

c = Cat()
c.speak()


# 3️⃣ Add new method
class Bird(Animal):
    def fly(self):
        print("Flying")

b = Bird()
b.fly()


# 4️⃣ Check type
print(isinstance(d, Animal))


# 5️⃣ Multiple children
class Fish(Animal):
    pass

f = Fish()
f.speak()
