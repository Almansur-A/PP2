import math
import random

# 1️⃣ Built-in math functions
print("Min:", min(3, 7, 1))
print("Max:", max(3, 7, 1))
print("Absolute:", abs(-15))
print("Round:", round(3.5678, 2))
print("Power:", pow(3, 3))

# 2️⃣ math module functions
print("Square root:", math.sqrt(25))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.9))
print("Pi:", math.pi)
print("Euler's number:", math.e)

# 3️⃣ Trigonometry
print("Sin(90°):", math.sin(math.radians(90)))
print("Cos(0°):", math.cos(math.radians(0)))

# 4️⃣ Random numbers
print("Random float:", random.random())
print("Random int:", random.randint(1, 100))

# 5️⃣ Random choice and shuffle
fruits = ["apple", "banana", "cherry", "orange"]
print("Random fruit:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled fruits:", fruits)

# 6️⃣ Random sample
print("Random sample:", random.sample(fruits, 2))
#EXAMPLES FROM THE TASK4
#Write a Python program to convert degree to radian.
import math
x = int(input())
y=math.radians(x)
print(y)
#Write a Python program to calculate the area of a trapezoid.
height = int(input())
base1 = int(input())
base2 = int(input())

area = (base1 + base2) / 2 * height

print("Area of trapezoid:", area)
# Regular Polygon Area
n = int(input())
s = int(input())

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", int(area))
# Parallelogram Area

base = int(input())
height = int(input())

area = base * height

print("Area of parallelogram:", float(area))