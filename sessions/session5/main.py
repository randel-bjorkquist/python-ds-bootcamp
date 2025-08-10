# ----------------------------------------------------------------------------------------------------------------------
# Session 5: Python Control Flow
print(f"Welcome to Session {5} - Control Flow!")

# Example: basic if-else
number = int(input("Enter a number: "))

if number > 0:
  print("Positive number!")
elif number == 0:
  print("Zero.")
else:
  print("Negative number.")
  
# ----------------------------------------------------------------------------------------------------------------------
score = 87

if score >= 90:
  print("Grade: A")
elif 80 <= score < 90:
  print("Grade: B")
else:
  print("Grade: C or lower")

# Logical operators
age = 30

if age < 18 or age > 65:
  print("You get a discount!")
else:
  print("Regular price.")

is_admin = False

if not is_admin:
  print("Access denied.")

# ----------------------------------------------------------------------------------------------------------------------
print()

# ----------------------------------------------------------------------------------------------------------------------
# Loops (for and while)
for color in ['red', 'green', 'blue']:
  print(f"{color} is {color.capitalize()}")

print()

_0_to_5_by_1 = range(5)       # output: 0, 1, 2, 3, 4
_0_to_6_by_2 = range(0, 8, 2) # output: 0, 2, 4, 6
_0_to_8_by_2 = range(0, 9, 2) # output: 0, 2, 4, 6

for i in range(5):
  print(i)

print()

colors = ['red', 'green', 'blue']

for index, color in enumerate(colors, start = 1):
  print(f"{index:} {color}")

print()

person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key, value in person.items():
  print(f"{key} -> {value}")

names = ["Bob", "", "Alice", None, "Charlie"]

for name in names:
  if not name:    # short-cut, same as -> if name not in("", None):
    continue
  print(name)

print()

# ----------------------------------------------------------------------------------------------------------------------
### While Loops Overview
# Basic syntax:

count = 0

while count < 5:
    print(count)
    count += 1
