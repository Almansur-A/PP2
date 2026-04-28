# 1️⃣ Instance method
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(3, 4))


# 2️⃣ Another instance method
    def multiply(self, a, b):
        return a * b


# 3️⃣ Using self
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

p = Person("Alice")
print(p.greet())


# 4️⃣ Method calling another method
class Example:
    def first(self):
        return "First"

    def second(self):
        return self.first() + " Second"

e = Example()
print(e.second())


# 5️⃣ Real-world example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount(100)
print(account.deposit(50))
