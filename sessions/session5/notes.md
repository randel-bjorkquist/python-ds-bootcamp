# Session 5: Control Flow (if/elif/else, logic, loops)

## Topics
- If, elif, else statements
- Comparison and logical operators
- Input validation
- For and while loops
- Real-world exercises

### Mini-Challenge (Try in mini-exercises.py):

Ask the user for their age. Print:

    "You are a minor." if under 18

    "You are an adult." if 18 to 64 (inclusive)

    "You are a senior." if 65+

### Input Validation (Basics)

In Python, the simplest way to validate user input is to:

    Wrap conversions (int(), float()) in try/except blocks.

    Loop until valid input is received.

    Optionally strip whitespace and normalize case.

Example: Integer input with retry
```python
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

age = get_int("Enter your age: ")
print(f"Your age is {age}")
```

Example: Float input with range check
```python
def get_float_in_range(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt).strip())
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid number. Please try again.")

temp = get_float_in_range("Enter temperature in Fahrenheit: ", 90.0, 110.0)
print(f"Valid temperature entered: {temp}")
```

### Mini-Exercise – get_yes_no() Function
Write a function called get_yes_no(prompt) that:

    Loops until the user enters yes or no (case-insensitive).

    Returns True if they enter "yes", and False if they enter "no".

    Ignores any surrounding spaces in the input.

#### Extra credit:
    Let "y" count as "yes" and "n" count as "no".

    Make it so the function always returns a Boolean (True or False) without throwing an error.

Example run:
```pgsql
Do you like Python? maybe
Please enter 'yes' or 'no'.
Do you like Python? YES
True
```

