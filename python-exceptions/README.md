
# Python Errors and Exceptions — Learning Repository

This repository contains notes, examples, and exercises to learn about errors and exceptions in Python. It is designed for self-study and hands-on practice.

## Learning Objectives

- **What's the difference between errors and exceptions**: Understand syntax/runtime errors vs. exceptions raised at runtime, and how Python represents them (Tracebacks vs. Exception objects).
- **What are exceptions and how to use them**: Learn what exceptions are, common built-in exceptions, and how to use `try`, `except`, `else`, and `finally` blocks.
- **When do we need to use exceptions**: Learn when to rely on exceptions for abnormal situations, input validation, resource handling, and guarding against unexpected states.
- **How to correctly handle an exception**: Explore catching specific exception types, avoiding bare `except`, preserving tracebacks, and using exception chaining when appropriate.
- **What's the purpose of catching exceptions**: Learn to maintain program stability, provide helpful error messages, and recover or fail gracefully.
- **How to raise a builtin exception**: Examples of using `raise` with built-in exceptions (e.g., `ValueError`, `TypeError`, `RuntimeError`) and raising with informative messages.
- **When do we need to implement a clean-up action after an exception**: Understand `finally`, context managers (`with`), and when to release resources or rollback state after an exception.

## Quick Examples

```py
# Catching specific exceptions
try:
 value = int(input("Enter a number: "))
except ValueError as e:
 print("Please enter a valid integer.")
else:
 print("You entered:", value)
finally:
 print("Input attempt complete.")

# Raising a built-in exception
def set_age(age):
 if age < 0:
  raise ValueError("age must be >= 0")
```

## Exercises

- Implement a function that reads integers from a file and handles malformed lines gracefully.
- Write code that opens a network/socket resource and ensures it is always closed, even on errors.
- Create a small CLI that demonstrates raising and catching custom exceptions.

## Suggested Next Steps

- Study common built-in exceptions in the Python docs.
- Practice converting try/finally patterns into context managers.
- Submit a PR with solutions to the exercises.

---
Happy learning! If you want, I can add example files or exercises with tests next.
