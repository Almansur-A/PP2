# Example 1: Break in while
i = 1
while True:
    if i > 3:
        break
    print(i)
    i += 1

# Example 2: Break on condition
n = 0
while n < 10:
    if n == 5:
        break
    print(n)
    n += 1

# Example 3: User input break
while True:
    s = input("Type 'stop' to break: ")
    if s == "stop":
        break

# Example 4: Break even numbers
i = 0
while True:
    if i % 2 == 0 and i > 6:
        break
    print(i)
    i += 1

# Example 5: Infinite loop with break
x = 1
while True:
    print(x)
    if x == 4:
        break
    x += 1
