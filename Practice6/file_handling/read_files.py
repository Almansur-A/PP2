f = open("example.txt", "r")
print(f.read())
f.close()

f = open("example.txt", "r")
print(f.readline())
f.close()

f = open("example.txt", "r")
print(f.readlines())
f.close()

with open("example.txt", "r") as f:
    print(f.read())