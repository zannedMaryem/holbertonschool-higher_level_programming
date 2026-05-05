# Python: If-Else, Loops, and Functions

A learning guide for understanding conditional statements, iteration structures, and functions in Python.

---

## Table of Contents

1. [Objectives](#objectives)
2. [If-Else Statements](#if-else-statements)
3. [Loops](#loops)
4. [Functions](#functions)
5. [Best Practices](#best-practices)
6. [Common Patterns](#common-patterns)

---

## Objectives

By the end of this guide, you will understand:

- **Indentation** — Why indentation is so important in Python and how it defines code blocks
- **If-Else Statements** — How to use the `if`, `if...else` statements to make decisions
- **Comments** — How to use comments to document and explain your code
- **Variable Assignment** — How to assign values to variables
- **While and For Loops** — How to use `while` and `for` loops to repeat code
- **Break and Continue** — How to use the `break` and `continue` statements to control loop flow
- **Else Clauses on Loops** — How to use `else` clauses with loops for post-loop execution
- **Pass Statement** — What the `pass` statement does and when to use it
- **Range Function** — How to use `range()` to generate sequences of numbers
- **Functions** — What a function is and how to define and use functions
- **Return Statement** — What a function returns when it doesn't use any `return` statement
- **Variable Scope** — Understanding the scope of variables (local, global, etc.)
- **Traceback** — What a traceback is and how to read error messages
- **Arithmetic Operators** — What the arithmetic operators are and how to use them

---

## Indentation

Indentation is critical in Python—it defines code blocks and determines which statements are part of loops, functions, conditionals, and classes.

### Why Indentation Matters

```python
# Correct - The print statement is indented
if age >= 18:
    print("You are an adult")

# Wrong - IndentationError
if age >= 18:
print("You are an adult")
```

### Indentation Rules

- Use **4 spaces** per indentation level (or 1 tab)
- Be consistent throughout your file
- Indentation indicates code blocks for: `if`, `elif`, `else`, `for`, `while`, `def`, `class`, etc.

```python
for i in range(3):           # No indent
    print(i)                 # 1 level indent (inside for loop)
    if i == 1:               # 1 level indent (inside for loop)
        print("Found it!")   # 2 level indent (inside if, inside for)
```

---

## Comments

Comments allow you to explain your code without affecting execution.

### Single-line Comments

```python
# This is a comment
age = 25  # You can also comment at the end of a line
```

### Multi-line Comments

```python
# This is a comment
# that spans multiple
# lines

"""
This is a docstring, often used for functions
and classes to describe their purpose
"""
```

### When to Use Comments

```python
# Good - explains WHY
result = value * 1.08  # 8% sales tax calculation

# Avoid - explains WHAT (obvious from code)
result = value * 1.08  # Multiply value by 1.08

# Good - docstring for functions
def calculate_tax(price):
    """Calculate sales tax at 8% rate"""
    return price * 1.08
```

---

## Variable Assignment

Variables store values that you can use throughout your program.

### Basic Assignment

```python
name = "Alice"          # String
age = 30                # Integer
height = 5.8            # Float
is_student = True       # Boolean
```

### Multiple Assignment

```python
# Assign multiple variables
x, y, z = 1, 2, 3

# Swap variables
a, b = 5, 10
a, b = b, a  # Now a=10, b=5

# Unpack lists
colors = ["red", "green", "blue"]
first, second, third = colors
```

### Variable Naming Rules

```python
# Valid names
name = "Alice"
_private_var = 10
variable123 = 5

# Invalid names (will cause errors)
# 123variable = 5        # Can't start with number
# var-name = 5           # Can't use hyphens
# var name = 5           # Can't use spaces
# if = 5                 # Can't use reserved keywords
```

---

## Arithmetic Operators

Python supports standard mathematical operations.

### Basic Operators

```python
# Addition
result = 10 + 5  # 15

# Subtraction
result = 10 - 5  # 5

# Multiplication
result = 10 * 5  # 50

# Division (returns float)
result = 10 / 5  # 2.0

# Floor Division (returns integer)
result = 10 // 3  # 3

# Modulo (remainder)
result = 10 % 3  # 1

# Exponentiation
result = 2 ** 3  # 8
```

### Operator Precedence (PEMDAS)

```python
# Parentheses first
result = (2 + 3) * 4  # 20

# Then exponentiation
result = 2 + 3 * 4  # 14 (multiplication before addition)

# Multiplication/Division (left to right)
result = 10 / 2 * 5  # 25

# Full expression
result = 2 + 3 ** 2 * 4 - 1  # 2 + 9 * 4 - 1 = 2 + 36 - 1 = 37
```

### Augmented Assignment

```python
x = 10

x += 5   # x = x + 5 = 15
x -= 3   # x = x - 3 = 12
x *= 2   # x = x * 2 = 24
x /= 4   # x = x / 4 = 6.0
x //= 2  # x = x // 2 = 3
x %= 2   # x = x % 2 = 1
x **= 2  # x = x ** 2 = 1
```

---

Conditional statements allow your program to make decisions based on conditions.

### Basic Syntax

```python
if condition:
    # Code executed if condition is True
elif other_condition:
    # Code executed if other_condition is True
else:
    # Code executed if none of the above conditions are True
```

### Examples

#### Simple If-Else

```python
age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

#### Multiple Conditions (elif)

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

#### Nested If-Else

```python
age = 25
income = 50000

if age >= 18:
    if income > 30000:
        print("Eligible for loan")
    else:
        print("Income too low")
else:
    print("Too young to apply")
```

#### Ternary Operator

```python
status = "Adult" if age >= 18 else "Minor"
print(status)
```

#### Logical Operators

```python
age = 20
income = 40000

# AND operator
if age >= 18 and income >= 35000:
    print("Eligible for premium membership")

# OR operator
if age < 13 or age > 65:
    print("Eligible for discount")

# NOT operator
if not is_member:
    print("Please become a member")
```

---

## Loops

Loops allow you to repeat blocks of code multiple times.

### For Loops

Iterate a specific number of times or through a collection.

#### Iterate Through a Range

```python
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

#### Iterate Through a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

#### Iterate With Index

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # Output: 0: apple, 1: banana, 2: cherry
```

#### Range Parameters

```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 5):
    print(i)  # 2, 3, 4

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

#### Iterate Through Dictionary

```python
person = {"name": "Alice", "age": 30, "city": "Paris"}

for key, value in person.items():
    print(f"{key}: {value}")
```

### While Loops

Execute code as long as a condition is True.

#### Basic While Loop

```python
count = 0

while count < 5:
    print(count)
    count += 1  # Increment count
    # Output: 0, 1, 2, 3, 4
```

#### While Loop With Break

```python
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

#### While Loop With Continue

```python
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop
    print(count)  # Output: 1, 2, 4, 5
```

### Loop Control

```python
# break: Exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue: Skip to the next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4

# else: Execute after loop completes normally
for i in range(3):
    print(i)
else:
    print("Loop completed!")
```

---

## Functions

Functions are reusable blocks of code that perform specific tasks.

### Function Definition

```python
def function_name(parameters):
    """Docstring describing what the function does"""
    # Function body
    return result
```

### Basic Function

```python
def greet():
    print("Hello, World!")

greet()  # Call the function
```

### Function With Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

### Function With Return Value

```python
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### Multiple Return Values

```python
def get_user_info():
    name = "Alice"
    age = 30
    return name, age

name, age = get_user_info()
print(f"{name} is {age} years old")
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Output: Hello, Alice!
greet("Bob", "Hi")       # Output: Hi, Bob!
```

### Variable Number of Arguments

```python
# *args: Non-keyword arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# **kwargs: Keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Paris")
# Output:
# name: Alice
# age: 30
# city: Paris
```

### Nested Functions

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(3))  # Output: 8
```

### Lambda Functions

```python
# Anonymous function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Using with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Using with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
```

### Return Statement

Every function returns a value:

```python
# Explicit return
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Function without return statement returns None
def greet(name):
    print(f"Hello, {name}!")
    # Implicitly returns None

greeting_result = greet("Alice")
print(greeting_result)  # None
```

---

## Pass Statement

The `pass` statement is a null operation—when executed, nothing happens. It's used as a placeholder when a statement is required but no code needs to be executed.

### When to Use Pass

```python
# Placeholder for a function you'll implement later
def calculate_result():
    pass  # TODO: implement this function

# Placeholder in a loop
for i in range(5):
    if i == 2:
        pass  # Do nothing when i equals 2
    else:
        print(i)

# Placeholder in conditionals
if user_input == "skip":
    pass  # Do nothing for skip
else:
    process(user_input)

# Placeholder in class definition
class MyClass:
    pass  # Empty class definition

# Placeholder in exception handling
try:
    risky_operation()
except ValueError:
    pass  # Ignore this error for now
```

### Without Pass (Causes IndentationError)

```python
# This will cause an error
def my_function():
    # IndentationError: expected an indented block

# Solution: Use pass
def my_function():
    pass
```

---

## Range Function

The `range()` function generates a sequence of numbers.

### Range Syntax

```python
# range(stop) - 0 to stop-1
list(range(5))  # [0, 1, 2, 3, 4]

# range(start, stop) - start to stop-1
list(range(2, 7))  # [2, 3, 4, 5, 6]

# range(start, stop, step)
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### Using Range in Loops

```python
# Count from 0 to 9
for i in range(10):
    print(i)

# Count from 1 to 10 (inclusive)
for i in range(1, 11):
    print(i)

# Count by tens
for i in range(0, 100, 10):
    print(i)  # 0, 10, 20, 30, ...

# Countdown
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1

# Use with len() to iterate by index
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

---

## Variable Scope

Variable scope determines where a variable can be accessed.

### Local Scope

Variables defined inside a function are local to that function.

```python
def my_function():
    x = 10  # Local variable
    print(x)  # 10

my_function()
print(x)  # NameError: name 'x' is not defined
```

### Global Scope

Variables defined outside functions are global and can be accessed anywhere.

```python
x = 10  # Global variable

def my_function():
    print(x)  # Can access global x

my_function()  # 10
print(x)  # 10
```

### Global Keyword

Use `global` keyword to modify a global variable inside a function.

```python
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # 20

# Without global keyword
y = 10

def modify_local():
    y = 20  # Creates a new local variable
    print(y)  # 20

modify_local()
print(y)  # 10 (unchanged)
```

### Nonlocal Scope

Use `nonlocal` for nested functions to access variables from enclosing scope.

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
    
    inner()
    print(x)  # 20

outer()
```

### Scope Hierarchy

```python
# Global scope
global_var = "global"

def outer_function():
    # Outer local scope
    outer_var = "outer"
    
    def inner_function():
        # Inner local scope
        inner_var = "inner"
        print(global_var)   # Can access global
        print(outer_var)    # Can access outer
        print(inner_var)    # Can access inner
    
    inner_function()
    # print(inner_var)  # NameError: can't access inner scope

outer_function()
```

---

## Else Clauses on Loops

The `else` clause on a loop executes when the loop completes normally (not interrupted by `break`).

### Else With For Loop

```python
# Else executes when loop completes
for i in range(3):
    print(i)
else:
    print("Loop completed!")

# Output:
# 0
# 1
# 2
# Loop completed!
```

### Else With For Loop and Break

```python
# Else does NOT execute when loop is interrupted
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print")

# Output:
# 0
# 1
# 2
```

### Else With While Loop

```python
# Else executes when while loop condition becomes False
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed!")

# Output:
# 0
# 1
# 2
# While loop completed!
```

### Practical Example: Search Pattern

```python
# Find a value in a list
items = [1, 2, 3, 4, 5]
search_value = 6

for item in items:
    if item == search_value:
        print(f"Found {search_value}!")
        break
else:
    print(f"{search_value} not found in list")

# Output: 6 not found in list
```

---

## Traceback

A traceback is an error report that shows where an error occurred in your code.

### Understanding Tracebacks

```python
def divide(a, b):
    return a / b

def calculate():
    result = divide(10, 0)
    return result

calculate()
```

**Output:**

```
Traceback (most recent call last):
  File "script.py", line 6, in <module>
    calculate()
  File "script.py", line 5, in calculate
    result = divide(10, 0)
  File "script.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```

### Reading a Traceback

1. **Error Type** — `ZeroDivisionError` (what went wrong)
2. **Error Message** — `division by zero` (why it failed)
3. **Call Stack** — Shows the sequence of function calls leading to the error
4. **File and Line** — Points to exactly where the error occurred

### Common Traceback Errors

```python
# NameError
print(undefined_variable)
# NameError: name 'undefined_variable' is not defined

# TypeError
print("hello" + 5)
# TypeError: can only concatenate str (not "int") to str

# ValueError
int("not a number")
# ValueError: invalid literal for int() with base 10: 'not a number'

# IndexError
my_list = [1, 2, 3]
print(my_list[10])
# IndexError: list index out of range

# KeyError
my_dict = {"name": "Alice"}
print(my_dict["age"])
# KeyError: 'age'
```

### How to Debug Using Traceback

1. Read the **error type** and **message**
2. Look at the **file and line number** where the error occurred
3. Examine the **call stack** to understand how you got there
4. Review your code at that location
5. Fix the issue and test again

---

## Best Practices

### 1. Use Meaningful Names

```python
# Good
for student in students:
    print(student.name)

# Avoid
for s in students:
    print(s.name)
```

### 2. Keep Functions Small and Focused

```python
# Good - Single responsibility
def validate_email(email):
    return "@" in email

def send_email(email):
    if validate_email(email):
        # Send email
        pass

# Avoid - Multiple responsibilities
def process_user(email):
    # Validate
    # Send
    # Log
    pass
```

### 3. Use Early Returns

```python
# Good
def process(value):
    if value is None:
        return None
    if value < 0:
        return 0
    # Main logic
    return value * 2

# Avoid
def process(value):
    if value is not None:
        if value >= 0:
            # Main logic
            return value * 2
```

### 4. Avoid Magic Numbers

```python
# Good
MAX_ATTEMPTS = 3
for attempt in range(MAX_ATTEMPTS):
    # Try something

# Avoid
for attempt in range(3):
    # Try something
```

### 5. Use Docstrings

```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numeric values
    
    Returns:
        Float: The average of the numbers
    """
    return sum(numbers) / len(numbers)
```

---

## Common Patterns

### Pattern 1: Validating Input

```python
def get_positive_number():
    while True:
        value = input("Enter a positive number: ")
        try:
            num = int(value)
            if num > 0:
                return num
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Invalid input. Please enter a number")
```

### Pattern 2: Processing a List

```python
def process_items(items):
    results = []
    for item in items:
        if is_valid(item):
            results.append(transform(item))
    return results
```

### Pattern 3: Conditional Task Execution

```python
def execute_task(task_type, data):
    if task_type == "add":
        return sum(data)
    elif task_type == "multiply":
        result = 1
        for num in data:
            result *= num
        return result
    elif task_type == "find_max":
        return max(data)
    else:
        return None
```

### Pattern 4: Accumulator Pattern

```python
def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total
```

---

## Summary

| Concept | Purpose | Example |
|---------|---------|---------|
| **If-Else** | Make decisions in code | `if age >= 18: print("Adult")` |
| **For Loop** | Iterate through collections | `for item in list: print(item)` |
| **While Loop** | Repeat while condition is true | `while count < 10: count += 1` |
| **Function** | Reuse code and organize logic | `def greet(name): print(f"Hi {name}")` |

---

## Practice Exercises

1. Write a function that checks if a number is positive, negative, or zero
2. Create a loop that prints multiplication table from 1 to 10
3. Write a function that returns the factorial of a number
4. Create a program that validates user input using a while loop
5. Write a function that finds the largest number in a list

---

**Happy Learning!** 🐍
