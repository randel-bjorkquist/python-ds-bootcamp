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

# Yes/No
yes = ask("Continue? (y/n): "
          ,choices = {'y': True, 'yes': True, 'n': False, 'no': False}
          ,normalize = lambda s: s.strip().lower())

# Float in range
temp = ask("Temp (F): "
           ,parser = float
           ,validate = lambda t: 90.0 <= t <= 110.0
           ,retry_msg = "Enter a number between 90 and 110.")

# Int with default
count = ask("How many items [default 3]: "
            ,parser = int
            ,default = 3)

quit()

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
