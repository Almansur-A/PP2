# 1️⃣ Class variable
class Dog:
    species = "Canine"

d1 = Dog()
d2 = Dog()
print(d1.species, d2.species)


# 2️⃣ Instance variable
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Bob")
print(p1.name, p2.name)


# 3️⃣ Changing class variable
Dog.species = "Animal"
print(d1.species)


# 4️⃣ Override class variable in instance
d1.species = "Custom"
print(d1.species, d2.species)


# 5️⃣ Counter example
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
print(Counter.count)
