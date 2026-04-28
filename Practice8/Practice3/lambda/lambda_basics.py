# 1️⃣ Simple lambda
double = lambda x: x * 2
print(double(5))


# 2️⃣ Lambda with two arguments
add = lambda a, b: a + b
print(add(3,4))


# 3️⃣ Lambda inside function
def apply(func, value):
    return func(value)

print(apply(lambda x: x**2, 5))


# 4️⃣ Conditional lambda
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))


# 5️⃣ Compare lambda vs normal function
def square(x):
    return x*x

print(square(6))
print((lambda x: x*x)(6))
