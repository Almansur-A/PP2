# 1️⃣ Simple function without arguments
def say_hello():
    print("Hello!")

say_hello()


# 2️⃣ Function with one argument
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# 3️⃣ Function returning a value
def square(number):
    return number * number

print(square(4))


# 4️⃣ Function with multiple arguments
def add(a, b):
    return a + b

print(add(5, 3))


# 5️⃣ Function with docstring
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

print(multiply(3, 6))
