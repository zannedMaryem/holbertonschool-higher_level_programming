# Python: Everything Is an Object

This README is a study guide for understanding one of the most important ideas in Python: everything is an object.

## Objectives

By the end of this guide, you should be able to:

- Understand what an object is.
- Explain the difference between a class and an object (or instance).
- Distinguish between immutable and mutable objects.
- Understand what a reference is.
- Understand what assignment means in Python.
- Explain what an alias is.
- Know how to check whether two variables are identical.
- Know how to check whether two variables refer to the same object.
- Display a variable's identifier (memory address in CPython).
- Understand how Python passes variables to functions.

---

## 1. What is an object?

In Python, almost everything is an object. An object is a value stored in memory that has:

- an identity (its unique id),
- a type,
- a value.

```python
# This example shows that a number is an object in Python.
a = 42
print(a)                 # Show the value of the variable.
print(type(a))           # Show the type of the object.
print(id(a))             # Show the object's identity (memory address in CPython).
```

---

## 2. What is the difference between a class and an object (or instance)?

A class is a blueprint or template for creating objects. An object (or instance) is a concrete item created from that class.

```python
# This defines a class called Dog.
class Dog:
    def __init__(self, name):
        self.name = name

# This creates an object (instance) of the Dog class.
my_dog = Dog("Buddy")

print(my_dog.name)       # Access the object's attribute.
```

---

## 3. What is the difference between an immutable object and a mutable object?

- An immutable object cannot be changed after it is created.
- A mutable object can be changed after it is created.

```python
# Immutable example: strings cannot be changed in place.
text = "hello"
# text[0] = "H"  # This would raise an error.

# Mutable example: lists can be changed.
numbers = [1, 2, 3]
numbers.append(4)       # Add a new element to the list.
print(numbers)
```

---

## 4. What is a reference?

A reference is a name that points to an object. In Python, variables are references to objects.

```python
# This shows that the variable points to an object.
a = [1, 2, 3]
print(a)                 # Print the list object.
```

---

## 5. What is an assignment?

Assignment gives a variable a reference to an object.

```python
# Assignment binds the name x to the integer object 10.
x = 10
print(x)
```

---

## 6. What is an alias?

An alias happens when two variables refer to the same object.

```python
# Create one object and give it two names.
a = [1, 2, 3]
b = a

# Both names point to the same list object.
print(b)
print(a is b)            # True because they are the same object.
```

---

## 7. How to know if two variables are identical

To check whether two variables have the same value, use `==`.

```python
# This checks whether the values are equal.
a = 5
b = 5
print(a == b)            # True because both values are 5.
```

---

## 8. How to know if two variables are linked to the same object

To check whether two variables point to the same object, use `is`.

```python
# This checks whether the two variables reference the same object.
a = [1, 2, 3]
b = a
print(a is b)            # True because b is an alias of a.
```

You can also compare identities using `id()`:

```python
# This shows the same idea using the object id.
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))    # True because both refer to the same object.
```

---

## 9. How to display the variable identifier (memory address in CPython)

Use the built-in `id()` function.

```python
# This prints the memory address of the object.
value = "Python"
print(id(value))
```

---

## 10. What is mutable and immutable?

- Mutable: the object can be changed after creation.
- Immutable: the object cannot be changed after creation.

```python
# Mutable example: a list can be modified.
mutable_list = [1, 2, 3]
mutable_list.append(4)
print(mutable_list)

# Immutable example: a tuple cannot be modified.
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10  # This would raise an error.
print(immutable_tuple)
```

---

## 11. What are the built-in mutable types?

Common built-in mutable types include:

- `list`
- `dict`
- `set`
- `bytearray`

```python
# These built-in types can be changed after creation.
my_list = [1, 2, 3]
my_list.append(4)

my_dict = {"name": "Alice"}
my_dict["age"] = 25

my_set = {1, 2, 3}
my_set.add(4)

print(my_list)
print(my_dict)
print(my_set)
```

---

## 12. What are the built-in immutable types?

Common built-in immutable types include:

- `int`
- `float`
- `str`
- `tuple`
- `bool`
- `None`
- `frozenset`
- `bytes`

```python
# These built-in types cannot be changed after creation.
number = 10
text = "hello"
values = (1, 2, 3)

print(number)
print(text)
print(values)
```

---

## 13. How does Python pass variables to functions?

Python passes arguments by object reference. This means the function receives the same object, but the variable name inside the function is local to that function.

### Example 1: Mutable object passed to a function

```python
# This function changes the list that was passed in.
def add_item(items):
    items.append("new")  # Modify the same list object.

my_list = ["old"]
add_item(my_list)
print(my_list)          # The change is visible outside the function.
```

### Example 2: Immutable object passed to a function

```python
# This function reassigns the local variable, but does not change the outer variable.
def change_number(x):
    x = 20              # Rebind the local name x to a new object.
    print("Inside function:", x)

value = 10
change_number(value)
print("Outside function:", value)   # The outer variable still points to 10.
```

### Example 3: The same object can be shared between arguments

```python
# This shows that two parameters can refer to the same object.
def show_identity(a, b):
    print(a is b)       # Check whether both arguments reference the same object.

shared = [1, 2, 3]
show_identity(shared, shared)
```

---

## Summary

The key idea is that Python variables are references to objects, not copies of objects. Understanding this helps explain:

- why changing a list inside a function can affect the original list,
- why strings and integers behave differently from lists,
- why `==` and `is` are different checks.
