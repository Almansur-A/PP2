# 1️⃣ Basic multiple inheritance
class Father:
    def skill(self):
        print("Gardening")

class Mother:
    def talent(self):
        print("Painting")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
c.talent()


# 2️⃣ Method resolution order
print(Child.__mro__)


# 3️⃣ Override from multiple parents
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.show()


# 4️⃣ Multiple inheritance with constructor
class Person:
    def __init__(self, name):
        self.name = name

class Worker:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Worker):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Worker.__init__(self, salary)

e = Employee("Alice", 5000)
print(e.name, e.salary)


# 5️⃣ Practical example
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()
