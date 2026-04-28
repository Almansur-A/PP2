# Example 1: Skip even numbers
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

# Example 2: Skip specific word
words = ["apple", "banana", "skip", "cherry"]
for w in words:
    if w == "skip":
        continue
    print(w)

# Example 3: Skip multiples of 3
for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i)

# Example 4: Skip negative numbers
nums = [1, -2, 3, -4, 5]
for n in nums:
    if n < 0:
        continue
    print(n)

# Example 5: Skip zeros
arr = [0, 1, 2, 0, 3]
for a in arr:
    if a == 0:
        continue
    print(a)
