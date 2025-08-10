# ----------------------------------------------------------------------------------------------------------------------
# ### CSV-style for-loop challenge
# You have a simulated CSV dataset stored in a list of strings, where the first line contains column headers and each
# subsequent line contains data.
#
# You need to:
# 1. Skip the header row.
# 2. Split each data row into columns.
# 3. Print the output in a clean, readable format.
#
# Starter Data
# csv_data = [ "name,age,city"
#             ,"Alice,30,New York"
#             ,"Bob,25,Los Angeles"
#             ,"Charlie,35,Chicago" ]
#
# Goal Output
# Name: Alice | Age: 30 | City: New York
# Name: Bob | Age: 25 | City: Los Angeles
# Name: Charlie | Age: 35 | City: Chicago

csv_data = [ "name,age,city"
            ,"Alice,30,New York"
            ,"Bob,25,Los Angeles"
            ,"Charlie,35,Chicago" ]

#--------------------------------------------------------------------------------------------------
# My Solution ...
#for row_index, row in enumerate(csv_data):
#  if row_index == 0:
#    column_headers = row.split(',')
#    continue
#  else:
#    row_data = row.split(',')
#
#    for column_index, column_header in enumerate(column_headers):
#      column_headers_length = len(column_headers) - 1
#
#      print( f"{column_header.title()}: {row_data[column_index]}"
#            ,end = ' | ' if column_index < column_headers_length else '\n')
#
#--------------------------------------------------------------------------------------------------
# ChatGPT's Solution
#headers = [header.strip() for header in csv_data[0].split(',')]
#
#for row in csv_data[1:]:
#  cells = [cell.strip() for cell in row.split(',')]
#  pairs = zip(headers, cells)
#
#  print(' | '.join(f"{header.title()}: {cell}" for header, cell in pairs))

#--------------------------------------------------------------------------------------------------
# NOTE: alternative wording/variable names ...

#keys = [header.strip() for header in csv_data[0].split(',')]
#keys = [item.strip() for item in csv_data[0].split(',')]
keys = [value.strip() for value in csv_data[0].split(',')]

for row in csv_data[1:]:  # NOTE [1:] means to skip the first row
  #cells = [cell.strip() for cell in row.split(',')]
  #cells = [item.strip() for item in row.split(',')]
  #cells = [value.strip() for value in row.split(',')]
  values = [value.strip() for value in row.split(',')]

  #pairs = zip(keys, cells)
  pairs = zip(keys, values)
 
  print(' | '.join(f"{key.title()}: {value}" for key, value in pairs))

#--------------------------------------------------------------------------------------------------
import csv, io

reader = csv.reader(io.StringIO("\n".join(csv_data)))
header = next(reader)
for row in reader:
  print(' | '.join(f"{key.title()}: {value}"  for key, value in zip(header, row)))


quit()  # uncomment to exit and not execute the exercises below

# ----------------------------------------------------------------------------------------------------------------------
### Mini-Exercise 1 — Filtering Names
# You have the following list:
# names = ["Alice", "", "Bob", None, "Charlie", "", "Diana"]
#
# Task:
# * Loop through the list and print each name in title case (first letter uppercase, rest lowercase).
# * Skip over any empty strings ("") or None values.

names = ["alice", "", "bob", None, "charlie", "", "diana"]

for name in names:
  if not name:
    continue
    
  print(name.title())

### Mini-Exercise 2 — Numbered Shopping List
# You have the following list:
# shopping_list = ["apples", "milk", "bread", "eggs"]
#
# Task:
# * Print a numbered list of items starting from 1.
# * The output should look like:
#   1. apples
#   2. milk
#   3. bread
#   4. eggs
# * Use enumerate() to make it happen.

shopping_list = ["apples", "milk", "bread", "eggs"]

for index, item in enumerate(shopping_list, start = 1):
  print(f"{index}. {item}")

# ----------------------------------------------------------------------------------------------------------------------
# Mini-Exercise – get_yes_no() Function
# Write a function called get_yes_no(prompt) that:
#     Loops until the user enters yes or no (case-insensitive).
#     Returns True if they enter "yes", and False if they enter "no".
#     Ignores any surrounding spaces in the input.

#yes_no_rules = [ (lambda v: v == 'yes' or v == 'y' ,True )
#                ,(lambda v: v == 'no'  or v == 'n' ,False)
#                ,(lambda v: None                   ,None )]
#
#for delegate, result in yes_no_rules:
#  if delegate(value):
#    return result
#    break

# NOTE: no real need for exception handling here, so remove the try-block
#def get_yes_no(prompt):
#  while True:
#    try:
#      value = input(prompt).strip().lower()
#
#      if value == 'yes' or value == 'y':
#        return True
#      elif value == 'no' or value == 'n':
#        return False
#      else:
#        raise ValueError()
#
#    except ValueError:
#      print("Please enter 'yes' or 'no'")

# NOTE: options given by ChatGPT - remove the try-block
#def get_yes_no(prompt):
#  while True:
#    value = input(prompt).strip().lower()
#
#    if value == 'yes' or value == 'y':
#      return True
#    elif value == 'no' or value == 'n':
#      return False
#    else:
#      print("Please enter 'yes' or 'no'")

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

# ----------------------------------------------------------------------------------------------------------------------
# Mini-Exercise (Asks the user for their temperature in Fahrenheit.)
# Prints:
#   "Normal body temperature" is between 97.0 and 99.0 (inclusive)
#   "Fever" if greater than 99.0
#   "Below normal" if less than 97.0

body_temperature = float(input("Enter your body temperature: "))

if body_temperature < 97.0:
  print("Below normal")
elif body_temperature > 99.0:
  print("Fever")
else:
  print("Normal body temperature")

# NOTE: given as a second option by ChatGPT
# if body_temperature < 97.0:
#   print("Below normal")
# elif 97.0 <= body_temperature <= 99.0:
#   print("Normal body temperature")
# else:
#   print("Fever")

# NOTE: given as a third option by ChatGPT
# print("Below normal" if body_temperature < 97.0 else "Fever" if body_temperature > 99.0 else "Normal body temperature")
# print( "Below normal" if body_temperature < 97.0 else
#        "Fever"        if body_temperature > 99.0 else
#        "Normal body temperature" )

# NOTE: given as a fourth option by ChatGPT
rules = [ (lambda t: t < 97.0 ,"Below normal")
         ,(lambda t: t > 99.0 ,"Fever")
         ,(lambda t: True     ,"Normal body temperature") ]

for pred, msg in rules:
  if pred(body_temperature):
    print(msg)
    break


# ----------------------------------------------------------------------------------------------------------------------
# Mini-Challenge (Ask the user for their age. Print):
#   "You are a minor." if under 18
#   "You are an adult." if 18 to 64 (inclusive)
#   "You are a senior." if 65+

age = int(input("Enter your age: "))

if age < 18:
  print("You are a minor.")
elif age > 64:
  print("You are a senior.")
else:
  print("You are an adult.")
