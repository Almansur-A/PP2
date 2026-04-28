# Example 1: Basic elif
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# Example 2: Multiple conditions
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Example 3: Grading system
marks = 72
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"
print(grade)

# Example 4: Age group
age = 18
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Example 5: Nested elif
x = 15
if x < 10:
    print("Less than 10")
elif x < 20:
    print("Between 10 and 19")
else:
    print("20 or more")
