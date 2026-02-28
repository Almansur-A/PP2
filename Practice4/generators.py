# 1️⃣ Using iter() and next()
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))

# 2️⃣ Loop through iterator manually
numbers2 = [1, 2, 3, 4]
it2 = iter(numbers2)
while True:
    try:
        print(next(it2))
    except StopIteration:
        break

# 3️⃣ Custom iterator class
class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

for x in MyNumbers():
    print(x)

# 4️⃣ Generator function
def count_down(n):
    while n > 0:
        yield n
        n -= 1

for num in count_down(5):
    print(num)

# 5️⃣ Fibonacci generator
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

for f in fibonacci(50):
    print(f)

# 6️⃣ Generator expression
squares = (x * x for x in range(6))
for s in squares:
    print(s)
#EXAMPLES FROM THE TASK4
# Squares up to N
def squares_up_to(n):
    for i in range(n + 1):
        yield i * i
for value in squares_up_to(5):
    print(value)

# Even numbers generator
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input())
print(",".join(str(num) for num in even_numbers(n)))

# Divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for num in divisible_by_3_and_4(n):
    print(num)

# Squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
for value in squares(3, 7):
    print(value)

# Countdown generator
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
for num in countdown(5):
    print(num)