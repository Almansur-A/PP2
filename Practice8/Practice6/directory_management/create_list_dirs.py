import os

os.makedirs("test_dir/sub_dir", exist_ok=True)

print(os.listdir("."))

print(os.getcwd())

os.chdir("test_dir")
print(os.getcwd())

os.chdir("..")

os.rmdir("test_dir/sub_dir")
os.rmdir("test_dir")