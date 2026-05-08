# Python Import and Modules

This README provides an overview of Python's import system and modules, covering the following objectives:

## Why Python Programming is Awesome

Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. It supports multiple programming paradigms, has a vast standard library, and a large ecosystem of third-party packages. Python is widely used in web development, data science, automation, and more, making it an excellent choice for beginners and experts alike.

## How to Import Functions from Another File

To import functions from another file, use the `import` statement. For example, if you have a file named `add_0.py` with a function `add`, you can import it in another file like `0-add.py`:

```python
from add_0 import add
```

This imports the `add` function specifically from the `add_0` module.

## How to Use Imported Functions

Once imported, you can use the function just like any other function in your code:

```python
a = 1
b = 2
result = add(a, b)
print("{} + {} = {}".format(a, b, result))
```

This will call the `add` function with arguments 1 and 2, and print the result.

## How to Create a Module

A module in Python is simply a `.py` file that contains Python code. To create a module, write your functions, classes, or variables in a `.py` file. For example, `add_0.py` is a module that defines the `add` function:

```python
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)
```

Any `.py` file can be imported as a module.

## How to Use the Built-in Function dir()

The `dir()` function returns a list of names in the current local scope or the attributes of an object. When used on a module, it shows all the names defined in that module:

```python
import add_0
print(dir(add_0))
```

This will output something like: `['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add']`

## How to Prevent Code in Your Script from Being Executed When Imported

To prevent code from running when a script is imported as a module, wrap it in an `if __name__ == "__main__":` block. This ensures the code only runs when the script is executed directly, not when imported:

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
```

Now, if you import `add_0`, the print statement won't execute.

## How to Use Command Line Arguments with Your Python Programs

You can access command line arguments using the `sys.argv` list from the `sys` module. `sys.argv[0]` is the script name, and subsequent elements are the arguments:

```python
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <num1> <num2>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
```

Run the script with: `python script.py 3 4`

This will output: `3 + 4 = 7`
