with open("example.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is a test file\n")

with open("example.txt", "a") as f:
    f.write("Appended line\n")

with open("example.txt", "r") as f:
    print(f.read())