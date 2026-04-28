# 1️⃣ Basic __init__
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)


# 2️⃣ Multiple attributes
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = Student("Bob", "A")
print(s.name, s.grade)


# 3️⃣ Default parameter
class User:
    def __init__(self, username, role="guest"):
        self.username = username
        self.role = role

u = User("admin")
print(u.role)


# 4️⃣ Modify attribute
u.role = "administrator"
print(u.role)


# 5️⃣ Delete attribute
del u.role
# print(u.role)  # This would raise an error
