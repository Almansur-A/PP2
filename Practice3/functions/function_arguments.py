# 1️⃣ Default parameter
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Bob")


# 2️⃣ Positional arguments
def describe_pet(animal, name):
    print(f"{name} is a {animal}")

describe_pet("dog", "Buddy")


# 3️⃣ Arbitrary arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))


# 4️⃣ Keyword arguments (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(key, value)

print_info(name="Alice", age=25)


# 5️⃣ Passing list as argument
def print_list(items):
    for item in items:
        print(item)

print_list(["apple", "banana", "cherry"])
