import shutil
import os

shutil.copy("example.txt", "copy_example.txt")

shutil.copy("example.txt", "backup_example.txt")

if os.path.exists("copy_example.txt"):
    os.remove("copy_example.txt")

if os.path.exists("backup_example.txt"):
    os.remove("backup_example.txt")