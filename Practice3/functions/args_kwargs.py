# 1️⃣ Example of *args
def print_numbers(*args):
    for n in args:
        print(n)

print_numbers(1,2,3)


# 2️⃣ Sum with *args
def total(*args):
    return sum(args)

print(total(5,10,15))


# 3️⃣ Example of **kwargs
def student_info(**kwargs):
    print(kwargs)

student_info(name="Bob", grade="A")


# 4️⃣ Mixed parameters
def example(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

example(1,2,3,4,name="Alice")


# 5️⃣ Real-world style usage
def order_food(*items, **details):
    print("Items:", items)
    print("Details:", details)

order_food("Pizza", "Burger", size="Large")
