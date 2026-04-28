# Example 1: Break in for
for i in range(5):
    if i == 3:
        break
    print(i)

# Example 2: Stop on negative
nums = [1, 2, -1, 3]
for n in nums:
    if n < 0:
        break
    print(n)

# Example 3: User input break
while True:
    x = input("Enter number (0 to exit): ")
    if x == "0":
        break

# Example 4: Break on string
words = ["apple", "banana", "stop", "cherry"]
for w in words:
    if w == "stop":
        break
    print(w)

# Example 5: First multiple of 5
for i in range(1, 20):
    if i % 5 == 0:
        print(i)
        break
