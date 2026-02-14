# 1️⃣ Square numbers
nums = [1,2,3]
print(list(map(lambda x: x*x, nums)))


# 2️⃣ Convert to uppercase
names = ["alice", "bob"]
print(list(map(lambda x: x.upper(), names)))


# 3️⃣ Add 10
print(list(map(lambda x: x+10, nums)))


# 4️⃣ Multiply list
print(list(map(lambda x: x*3, nums)))


# 5️⃣ Boolean transformation
print(list(map(lambda x: x>2, nums)))
