# Python Data Structures: Lists and Tuples

This repository contains examples and exercises for learning Python's fundamental data structures: lists and tuples.

## Table of Contents

1. [Lists](#lists)
   - [What are Lists and How to Use Them](#what-are-lists-and-how-to-use-them)
   - [Differences and Similarities Between Strings and Lists](#differences-and-similarities-between-strings-and-lists)
   - [Common List Methods](#common-list-methods)
   - [Lists as Stacks and Queues](#lists-as-stacks-and-queues)
   - [List Comprehensions](#list-comprehensions)
2. [Tuples](#tuples)
   - [What are Tuples and How to Use Them](#what-are-tuples-and-how-to-use-them)
   - [When to Use Tuples vs Lists](#when-to-use-tuples-vs-lists)
3. [Sequences](#sequences)
   - [What is a Sequence](#what-is-a-sequence)
   - [Tuple Packing](#tuple-packing)
   - [Sequence Unpacking](#sequence-unpacking)
4. [The del Statement](#the-del-statement)

## Lists

### What are Lists and How to Use Them

Lists are mutable sequences in Python that can contain elements of different types. They are ordered collections that allow you to store and manipulate data efficiently.

**Creating Lists:**

```python
# Empty list
empty_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Using list() constructor
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
```

**Accessing Elements:**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # apple
print(fruits[-1])   # cherry (last element)
print(fruits[1:3])  # ['banana', 'cherry'] (slicing)
```

**Modifying Lists:**

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"  # ['apple', 'orange', 'cherry']
fruits.append("grape")  # ['apple', 'orange', 'cherry', 'grape']
```

### Differences and Similarities Between Strings and Lists

**Similarities:**

- Both are sequences (ordered collections)
- Support indexing and slicing
- Can be iterated over with loops
- Have length (len())

**Differences:**

- **Mutability:** Lists are mutable (can be changed), strings are immutable
- **Element Types:** Lists can contain mixed types, strings contain only characters
- **Methods:** Lists have many modification methods, strings have fewer methods

```python
# String (immutable)
s = "hello"
s[0] = "H"  # TypeError!

# List (mutable)
lst = ["h", "e", "l", "l", "o"]
lst[0] = "H"  # Works: ['H', 'e', 'l', 'l', 'o']
```

### Common List Methods

**Adding Elements:**

```python
fruits = ["apple", "banana"]

# append() - add to end
fruits.append("cherry")  # ['apple', 'banana', 'cherry']

# insert() - add at specific position
fruits.insert(1, "orange")  # ['apple', 'orange', 'banana', 'cherry']

# extend() - add multiple elements
fruits.extend(["grape", "kiwi"])  # ['apple', 'orange', 'banana', 'cherry', 'grape', 'kiwi']
```

**Removing Elements:**

```python
fruits = ["apple", "banana", "cherry", "banana"]

# remove() - remove first occurrence
fruits.remove("banana")  # ['apple', 'cherry', 'banana']

# pop() - remove and return element at index (default: last)
last = fruits.pop()  # last = 'banana', fruits = ['apple', 'cherry']
first = fruits.pop(0)  # first = 'apple', fruits = ['cherry']

# clear() - remove all elements
fruits.clear()  # []
```

**Other Useful Methods:**

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - sort in place
numbers.sort()  # [1, 1, 2, 3, 4, 5, 6, 9]

# reverse() - reverse in place
numbers.reverse()  # [9, 6, 5, 4, 3, 2, 1, 1]

# index() - find index of element
index = numbers.index(4)  # 3

# count() - count occurrences
count = numbers.count(1)  # 2

# copy() - create shallow copy
copy_numbers = numbers.copy()
```

### Lists as Stacks and Queues

**Using Lists as Stacks (LIFO - Last In, First Out):**

```python
stack = []

# Push elements
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# Pop elements
top = stack.pop()  # top = 3, stack = [1, 2]
top = stack.pop()  # top = 2, stack = [1]
```

**Using Lists as Queues (FIFO - First In, First Out):**

```python
from collections import deque

# For queues, use deque (more efficient than list)
queue = deque([1, 2, 3])

# Enqueue
queue.append(4)  # deque([1, 2, 3, 4])

# Dequeue
front = queue.popleft()  # front = 1, queue = deque([2, 3, 4])

# With regular list (less efficient)
queue_list = [1, 2, 3]
queue_list.append(4)  # [1, 2, 3, 4]
front = queue_list.pop(0)  # front = 1, queue_list = [2, 3, 4]
```

### List Comprehensions

List comprehensions provide a concise way to create lists from existing iterables.

**Basic Syntax:**

```python
# [expression for item in iterable]
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

**Examples:**

```python
# Convert strings to uppercase
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
# ['HELLO', 'WORLD', 'PYTHON']

# Filter and transform
numbers = [1, 2, 3, 4, 5, 6]
result = [x*2 for x in numbers if x > 3]
# [8, 10, 12]

# Flatten nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sublist in nested for x in sublist]
# [1, 2, 3, 4, 5, 6]
```

## Tuples

### What are Tuples and How to Use Them

Tuples are immutable sequences in Python. Once created, their contents cannot be modified.

**Creating Tuples:**

```python
# Empty tuple
empty_tuple = ()

# Single element tuple (note the comma!)
single = (1,)  # or 1,

# Multiple elements
coordinates = (10, 20)
person = ("John", 25, "Engineer")

# Without parentheses (tuple packing)
point = 10, 20, 30
```

**Accessing Elements:**

```python
point = (10, 20, 30)
print(point[0])    # 10
print(point[-1])   # 30
print(point[1:3])  # (20, 30)
```

**Tuple Methods:**

```python
numbers = (1, 2, 3, 2, 4)

# count() - count occurrences
count = numbers.count(2)  # 2

# index() - find index
index = numbers.index(3)  # 2
```

### When to Use Tuples vs Lists

**Use Tuples when:**

- Data should not be modified (immutable)
- You need hashable objects (can be used as dictionary keys or set elements)
- You want to return multiple values from a function
- You need to ensure data integrity
- Performance is critical (tuples are slightly faster)

**Use Lists when:**

- You need to modify the data
- You need to add/remove elements frequently
- Order might change
- You need more built-in methods

```python
# Tuple as dictionary key
locations = {("New York", "NY"): "USA", ("London", "UK"): "GB"}

# Function returning multiple values
def get_user():
    return ("Alice", 30, "Developer")

name, age, job = get_user()
```

## Sequences

### What is a Sequence

A sequence is an ordered collection of items that can be accessed by index. Python has several sequence types:

- **Lists:** Mutable sequences
- **Tuples:** Immutable sequences
- **Strings:** Immutable sequences of characters
- **Range objects:** Immutable sequences of numbers

All sequences support:

- Indexing: `seq[0]`
- Slicing: `seq[1:3]`
- Length: `len(seq)`
- Iteration: `for item in seq`
- Membership testing: `item in seq`

### Tuple Packing

Tuple packing is creating a tuple by assigning multiple values to a single variable without parentheses.

```python
# Tuple packing
point = 10, 20, 30  # equivalent to (10, 20, 30)

# Often used in function returns
def get_coordinates():
    return 100, 200  # returns (100, 200)
```

### Sequence Unpacking

Sequence unpacking is assigning elements of a sequence to multiple variables.

```python
# Basic unpacking
x, y, z = (10, 20, 30)
# x=10, y=20, z=30

# Works with any sequence
name, age = ["Alice", 25]
a, b, c = "ABC"

# Extended unpacking (Python 3)
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2, 3, 4], last=5

# Swapping values
a, b = b, a  # tuple packing/unpacking
```

## The del Statement

The `del` statement removes variables, list elements, or attributes.

**Deleting Variables:**

```python
x = 10
del x  # x no longer exists
```

**Deleting List Elements:**

```python
numbers = [1, 2, 3, 4, 5]
del numbers[2]  # [1, 2, 4, 5]
del numbers[1:3]  # [1, 4, 5]
```

**Deleting Slices:**

```python
letters = ['a', 'b', 'c', 'd', 'e']
del letters[1:4]  # ['a', 'e']
```

**Deleting Entire Objects:**

```python
data = [1, 2, 3]
del data  # list object is deleted
```

Note: `del` removes references, not necessarily the objects themselves. Objects are garbage collected when no references remain.
