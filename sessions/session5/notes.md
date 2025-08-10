# Session 5: Control Flow (if/elif/else, logic, loops)

## Topics
- If, elif, else statements
- Comparison and logical operators
- Input validation
- For and while loops
- Real-world exercises

### Mini-Challenge (Try in mini-exercises.py):

Ask the user for their age and print:

    "You are a minor." if under 18
    "You are an adult." if 18 to 64 (inclusive)
    "You are a senior." if 65+

### Input Validation (Basics)

In Python, the simplest way to validate user input is to:
* Wrap conversions (int(), float()) in try/except blocks.
* Loop until valid input is received.
* Optionally strip whitespace and normalize case.

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
1. Loops until the user enters yes or no (case-insensitive).
2. Returns True if they enter "yes", and False if they enter "no".
3. Ignores any surrounding spaces in the input.

#### Extra credit:
* Let "y" count as "yes" and "n" count as "no".
* Make it so the function always returns a Boolean (True or False) without throwing an error.

Example run:
```pgsql
Do you like Python? maybe
Please enter 'yes' or 'no'.
Do you like Python? YES
True
```

```python
# ----------------------------------------------------------------------------------------------------------------------
# NOTE: options given by ChatGPT - combined "yes"/"y" and "no"/"n" checks into a membership test for cleaner code ...
def get_yes_no(prompt):
  while True:
    value = input(prompt).strip().lower()
    
    if value in ('yes', 'y'):
      return True
    elif value in ('no', 'n'):
      return False
    else:
      print("Please enter 'yes' or 'no'")

# ----------------------------------------------------------------------------------------------------------------------
# NOTE: option given by ChatGPT - aligns with the rules created for the body temperature exercise below, but with a list
#       vs lambda expressions
def get_yes_no_v2(prompt):
  # Data-driven mapping: normalize input to a boolean
  yes_no_rules = { 'yes': True , 'y': True
                  ,'no' : False, 'n': False }
  
  while True:
    value = input(prompt).strip().lower()
    
    if value in yes_no_rules:
      return yes_no_rules[value]
    
    print("Please enter 'yes' or 'no'")

# ----------------------------------------------------------------------------------------------------------------------
# NOTE: option given by ChatGPT - aligns with the rules created for the body temperature exercise below, using lambdas
def get_yes_no_v3(prompt):
  yes_no_rules = [ (lambda v: v in ('yes', 'y'), True)
                  ,(lambda v: v in ('no', 'n'), False) ]
  
  while True:
    value = input(prompt).strip().lower()
    
    for predicate, result in yes_no_rules:
      if predicate(value):
        return result
      
    print("Please enter 'yes' or 'no'")
  
# ----------------------------------------------------------------------------------------------------------------------
# NOTE: option given by ChatGPT - reusable, more generic function, kind of like a template
def ask(prompt, *, parser=None, choices=None, validate=None,
        default=None, normalize=str.strip, retry_msg=None):
  """
  A flexible input helper.

  - choices: dict of normalized input -> return value (e.g., {'y': True, 'yes': True})
  - parser: callable to convert input (e.g., int, float, lambda s: s.lower())
  - validate: callable(value) -> bool (e.g., lambda x: 90 <= x <= 110)
  - default: value returned if user submits empty input
  - normalize: callable to preprocess raw text (default: strip)
  """
  while True:
    raw = input(prompt)
    if raw == "" and default is not None:
      return default
    
    text = normalize(raw) if normalize else raw
    
    if choices is not None:
      if text in choices:
        return choices[text]
      print(retry_msg or "Please enter one of: " + ", ".join(choices.keys()))
      continue
    
    if parser is not None:
      try:
        val = parser(text)
      except Exception:
        print(retry_msg or "Invalid input. Please try again.")
        continue
      
      if validate and not validate(val):
        print(retry_msg or "Value not in accepted range. Please try again.")
        continue
      return val
    
    print(retry_msg or "Please enter a valid value.")

# ----------------------------------------------------------------------------------------------------------------------
#yes_no = get_yes_no('Do you have a question? (yes/no): ')
#yes_no = get_yes_no_v2('Do you have a question? (yes/no): ')
yes_no = get_yes_no_v3('Do you have a question? (yes/no): ')

#if yes_no:
#  print("Great, what's the question? ")
#else:
#  print("No worries; please come back when you do.")

# NOTE: Use of ternary operator suggested by ChatGPT
print("Great, what's the question?"
      if yes_no else
      "No worries; please come back when you do.")

# ASK Template (Yes/No)
yes = ask("Continue? (y/n): "
          ,choices = {'y': True, 'yes': True, 'n': False, 'no': False}
          ,normalize = lambda s: s.strip().lower())

# ASK Template (Float in range)
temp = ask("Temp (F): "
           ,parser = float
           ,validate = lambda t: 90.0 <= t <= 110.0
           ,retry_msg = "Enter a number between 90 and 110.")

# ASK Template (Int with default)
count = ask("How many items [default 3]: "
            ,parser = int
            ,default = 3)
```

### Loops — both for and while:
1. Iterate over collections (for)
2. Repeat logic until a condition is met (while)
3. Use break and continue effectively
4. Combine loops with input validation and rules-based logic

#### Basic for loop
* Iterates over each element in the list
* color takes on each value in turn

```python
for color in ["red", "green", "blue"]:
    print(color)

# output:
#    red
#    green
#    blue
```

#### Using range()
* range(start, stop, step) works like: start (inclusive), stop (exclusive), increment

```python
for i in range(5):
    print(i)

# output:
#   0
#   1
#   2
#   3
#   4

_0_to_5_by_1 = range(5)       # output: 0, 1, 2, 3, 4
_0_to_6_by_2 = range(0, 8, 2) # output: 0, 2, 4, 6
_0_to_8_by_2 = range(0, 9, 2) # output: 0, 2, 4, 6, 8

```

#### Looping with enumerate()
* enumerate() gives you both the index and the value
* start = 1 makes it human-friendly (starts counting from 1)

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors, start = 1):
    print(f"{index}: {color}")

# output:
#   1 red
#   2 green
#   3 blue
```

#### Looping over dictionaries
* .items() returns key–value pairs
* Useful for config files, JSON parsing, etc.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key} -> {value}")

# output:
#   name -> Alice
#   age -> 30
#   city -> New York
```
Practical Example
* continue skips to the next iteration without running the rest of the loop body
* Often used for filtering

```python
names = ["Bob", "", "Alice", None, "Charlie"]

for name in names:
    if not name:
        continue  # skip empty or None
    print(name.upper())

# output:
#   Bob
#   Alice
#   Charlie
```

### Mini-Exercise 1 — Filtering Names
You have the following list:

```python
names = ["Alice", "", "Bob", None, "Charlie", "", "Diana"]
```

Task:
* Loop through the list and print each name in title case (first letter uppercase, rest lowercase).
* Skip over any empty strings ("") or None values.

### Mini-Exercise 2 — Numbered Shopping List
You have:

```python
shopping_list = ["apples", "milk", "bread", "eggs"]
```

Task:
* Print a numbered list of items starting from 1.
* Use enumerate() to make it happen.
* The output should look like:

```markdown
1. apples
2. milk
3. bread
4. eggs
```

### CSV-style for-loop challenge
You have a simulated CSV dataset stored in a list of strings, where the first line contains column headers and each subsequent line contains data.

You need to:
1. Skip the header row.
2. Split each data row into columns.
3. Print the output in a clean, readable format.

Starter Data
```python
csv_data = [ "name,age,city"
            ,"Alice,30,New York"
            ,"Bob,25,Los Angeles"
            ,"Charlie,35,Chicago" ]
```

Goal Output
```python
Name: Alice | Age: 30 | City: New York
Name: Bob | Age: 25 | City: Los Angeles
Name: Charlie | Age: 35 | City: Chicago    
```

Solutions
```python
# ----------------------------------------------------------------------   
csv_data = [ "name,age,city"
            ,"Alice,30,New York"
            ,"Bob,25,Los Angeles"
            ,"Charlie,35,Chicago" ]

# Naming Option (headers/cells) -----------------------------
headers = [header.strip() for header in csv_data[0].split(',')]

for line in csv_data[1:]:
    cells = [cell.strip() for cell in line.split(',')]
    header_cell_pairs = zip(headers, cells)
    print(' | '.join(f"{key.title()}: {value}" for key, value in header_cell_pairs))

# Naming Option (keys/values) ------------------------------    
keys = [key.strip() for key in csv_data[0].split(',')]

for line in csv_data[1:]:    
    values = [value.strip() for value in line.split(',')]
    key_value_pairs = zip(keys, values)
    
    print(' | '.join(f"{key.title()}: {value}" for key, value in key_value_pairs))

# Naming Option (keys/values) ------------------------------    
keys = [value.strip() for value in csv_data[0].split(',')]

for line in csv_data[1:]:    
    values = [value.strip() for value in line.split(',')]
    key_value_pairs = zip(keys, values)
    
    print(' | '.join(f"{key.title()}: {value}" for key, value in key_value_pairs))

# Naming Option (keys/values) ------------------------------    
keys = [item.strip() for item in csv_data[0].split(',')]

for line in csv_data[1:]:    
    values = [item.strip() for item in line.split(',')]
    key_value_pairs = zip(keys, values)
    
    print(' | '.join(f"{key.title()}: {value}" for key, value in key_value_pairs))
        
# ----------------------------------------------------------------------   
import csv, io

reader  = csv.reader(io.StringIO('\n'.join(csv_data)))
headers = next(reader)

for row in reader:
    print(' | '.join(f"{key.title()}: {value}" for key, value in zip(headers, row)))
```


