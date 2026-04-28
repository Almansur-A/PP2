# Example 1: Simple while
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 2: Sum numbers
n = 5
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)

# Example 3: Multiples of 3
i = 3
while i <= 15:
    print(i)
    i += 3

# Example 4: Countdown
count = 5
while count > 0:
    print(count)
    count -= 1

# Example 5: User input
x = 0
while x != 5:
    x = int(input("Enter 5 to stop: "))
