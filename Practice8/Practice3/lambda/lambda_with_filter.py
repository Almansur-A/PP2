# 1️⃣ Filter even numbers
nums = [1,2,3,4,5]
print(list(filter(lambda x: x%2==0, nums)))


# 2️⃣ Filter positive numbers
nums2 = [-1,5,-3,8]
print(list(filter(lambda x: x>0, nums2)))


# 3️⃣ Filter long strings
words = ["hi", "hello", "python"]
print(list(filter(lambda x: len(x)>4, words)))


# 4️⃣ Filter divisible by 3
print(list(filter(lambda x: x%3==0, nums)))


# 5️⃣ Filter numbers greater than 2
print(list(filter(lambda x: x>2, nums)))
