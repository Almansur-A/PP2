names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for i, name in enumerate(names):
    print(i, name)

for name, score in zip(names, scores):
    print(name, score)

nums = [3, 1, 4, 2]
print(sorted(nums))

x = "123"
y = int(x)
z = float(x)

print(type(x), type(y), type(z))