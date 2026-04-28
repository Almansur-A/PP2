# Example 1: Skip even numbers
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Example 2: Skip negative numbers
nums = [-2, -1, 0, 1, 2]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1

# Example 3: Skip multiples of 3
i = 1
while i <= 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)

# Example 4: Skip zeros
arr = [0, 1, 2, 0, 3]
i = 0
while i < len(arr):
    if arr[i] == 0:
        i += 1
        continue
    print(arr[i])
    i += 1

# Example 5: Skip input "skip"
while True:
    x = input("Enter text (stop to exit): ")
    if x == "stop":
        break
    if x == "skip":
        continue
    print(x)
