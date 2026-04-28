# 1️⃣ Sort numbers descending
nums = [5,1,4,2]
print(sorted(nums, key=lambda x: -x))


# 2️⃣ Sort by string length
words = ["apple", "kiwi", "banana"]
print(sorted(words, key=lambda x: len(x)))


# 3️⃣ Sort list of tuples by second element
students = [("Alice",90), ("Bob",75)]
print(sorted(students, key=lambda x: x[1]))


# 4️⃣ Sort by last character
print(sorted(words, key=lambda x: x[-1]))


# 5️⃣ Sort by absolute value
nums2 = [-10,5,-3,2]
print(sorted(nums2, key=lambda x: abs(x)))
