# 1️⃣ Basic super usage
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Alice", "A")
print(s.name, s.grade)


# 2️⃣ Call parent method
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

d = Dog()
d.speak()


# 3️⃣ Extend parent constructor
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

e = Employee("Bob", 5000)
print(e.name, e.salary)


# 4️⃣ Multiple attributes
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

m = Manager("Anna", 6000, 500)
print(m.name, m.salary, m.bonus)


# 5️⃣ super() in method
class Example:
    def show(self):
        print("Parent")

class Child(Example):
    def show(self):
        super().show()
        print("Child")

c = Child()
c.show()
