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
