# 1️⃣ Return single value
def get_number():
    return 10

print(get_number())


# 2️⃣ Return multiple values
def get_coordinates():
    return 5, 10

x, y = get_coordinates()
print(x, y)


# 3️⃣ Conditional return
def check_even(num):
    if num % 2 == 0:
        return True
    return False

print(check_even(4))


# 4️⃣ Return list
def get_squares(numbers):
    return [n*n for n in numbers]

print(get_squares([1,2,3]))


# 5️⃣ Return string
def format_name(name):
    return name.upper()

print(format_name("alice"))
