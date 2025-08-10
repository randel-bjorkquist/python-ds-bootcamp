# Session 6 — Functions

### Purpose:
Introduce and practice creating reusable code blocks with functions in Python.
Focus on defining, calling, and passing data to functions, as well as understanding return values.

## Key Topics:
* Defining functions with def
* Parameters vs arguments
* Default parameter values
* Returning values with return
* Scope (local vs global variables)
* Docstrings and inline documentation
* Calling functions from other modules

### Example:
```python
def greet(name="World"):
    """Prints a greeting to the user."""
    print(f"Hello, {name}!")

greet("Randel")
greet()  # uses default
```

### Best Practices:
* Keep functions small and focused on a single task
* Use descriptive names
* Document behavior with docstrings
* Avoid side effects unless intentional