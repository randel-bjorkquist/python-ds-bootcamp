# Session 4 Notes

- Session: Python Language Basics
- Structure: variables, types, input/output, comments, formatting, basic logic
- Supplement: Pluralsight's "Python Fundamentals"

🟢 Python Naming Conventions (PEP 8)
Variables and Functions

    Use snake_case (all lowercase, words separated by underscores)

        Example: user_name, total_amount, calculate_sum()

Constants

    Use ALL_CAPS_WITH_UNDERSCORES

        Example: MAX_SIZE, DEFAULT_PORT

Classes

    Use PascalCase (first letter of each word capitalized, no underscores)

        Example: BankAccount, DataLoader

Modules and Files

    Use snake_case

        Example: my_module.py, data_utils.py

Private/Internal Variables/Functions

    Prefix with a single underscore

        Example: _helper_function, _temp_var

🚫 Avoid in Python:

    camelCase (like userName or doSomething) is not standard for functions or variables (it’s common in JavaScript, not Python)

    PascalCase for functions or variables (only for classes!)

🔎 Official Reference:

See PEP 8 — [Style Guide for Python Code (Naming Conventions section)](https://peps.python.org/pep-0008/#naming-conventions)

| Kind        | Example             | Convention    |
| ----------- | ------------------- | ------------- |
| Variable    | `user_name`         | snake\_case   |
| Function    | `calculate_total()` | snake\_case   |
| Constant    | `MAX_LENGTH`        | ALL\_CAPS     |
| Class       | `AccountManager`    | PascalCase    |
| Module/File | `account_utils.py`  | snake\_case   |
| Private var | `_temp_value`       | \_snake\_case |

🟦 Session 4: Type Conversion (Casting) in Python
Why Convert Types?

    input() always returns a string; math needs int or float

    Sometimes you need to print numbers as strings

    Boolean logic often relies on converting user input

| To Type | Function   | Example                                |
| ------- | ---------- | -------------------------------------- |
| int     | `int(x)`   | `int("42") → 42`                       |
| float   | `float(x)` | `float("3.14") → 3.14`                 |
| str     | `str(x)`   | `str(99) → "99"`                       |
| bool    | `bool(x)`  | `bool("") → False`, `bool("a") → True` |

```python
age_str = input("How old are you? ")
age = int(age_str)  # Convert string to int
print(f"In 10 years, you will be {age + 10} years old.")

price_str = input("What is the price? ")
price = float(price_str)  # Convert string to float
print(f"Double the price is {price * 2:.2f}")

number = 5
number_str = str(number)
print("Number as string:", number_str, "| Type:", type(number_str))

user_input = input("Enter something: ")
is_nonempty = bool(user_input)
print(f"Is input non-empty? {is_nonempty}")
```

🧠 Tips

    If user input might not be a valid int/float, use try/except to avoid crashes.

    Booleans in Python: bool("") is False, any non-empty string is True.

    For booleans from input, check for 'yes', 'true', etc., with .lower().strip()

# Session 4 Recap: Python Variables, Types, and Conversion

## ✅ Topics Covered

- **Variables:**  
  Declared by assignment (`name = "Randel"`), case-sensitive, PEP 8: `snake_case`

- **Basic Data Types:**  
  - `int` (integer): `age = 42`  
  - `float` (decimal): `weight = 195.6`  
  - `str` (string/text): `city = "Dallas"`  
  - `bool` (True/False): `is_active = True`

- **Input and Output:**  
  - `input()` always returns a string  
  - Use `f-strings` for formatted output (best practice):  
    `print(f"Hello, {name}!")`

- **Type Conversion (Casting):**  
  - `int("5")`, `float("3.14")`, `str(99)`, `bool("abc")`  
  - Convert input to `int`/`float` for math  
  - Format floats with `{:.2f}` in f-strings for money/decimals

- **Best Practices:**  
  - Variable and function names: **snake_case**  
  - Use f-strings for all output  
  - Handle user input carefully: cast as needed, consider `.strip().lower()` for yes/no
  - (Optional) Use `try/except` for robust input conversion (advanced)

- **Mini-Exercises Completed:**  
  - Created variables of multiple types  
  - Used input and f-strings  
  - Converted types for math and display  
  - Bonus: Calculated and formatted vacation budget and temperature conversion

---

**Ready for Session 5: Control Flow (if/else, logical ops, loops)!**
