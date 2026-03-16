import shutil
import os

os.makedirs("dir1", exist_ok=True)
os.makedirs("dir2", exist_ok=True)

with open("dir1/test.txt", "w") as f:
    f.write("Hello")

shutil.copy("dir1/test.txt", "dir2/test_copy.txt")

shutil.move("dir1/test.txt", "dir2/test_moved.txt")

files = os.listdir("dir2")
for f in files:
    if f.endswith(".txt"):
        print(f)