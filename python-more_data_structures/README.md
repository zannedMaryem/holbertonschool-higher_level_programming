# Python More Data Structures

This directory focuses on advanced data structures in Python, including sets, dictionaries, and functional programming concepts like lambda functions, map, filter, and reduce.

## Learning Goals

### Data Structures

- Understand the importance of choosing the right data structure for different use cases
- Learn how data structures affect performance and memory usage

### Why Python Programming is Awesome

- Python's simplicity and readability make it ideal for rapid development
- Extensive standard library and third-party packages
- Strong community support and versatility across domains
- Dynamic typing and automatic memory management

### Sets

- **What are sets**: Unordered collections of unique elements
- **How to use them**: Create sets with `set()` or `{}` syntax, add/remove elements
- **Common methods**:
  - `add(element)`: Add an element to the set
  - `remove(element)`: Remove an element (raises KeyError if not found)
  - `discard(element)`: Remove an element if it exists
  - `union(other_set)`: Return a new set with elements from both sets
  - `intersection(other_set)`: Return a new set with common elements
  - `difference(other_set)`: Return a new set with elements in this set but not in other
  - `symmetric_difference(other_set)`: Return a new set with elements in either set but not both
- **When to use sets vs lists**: Use sets when you need unique elements and don't care about order. Sets are faster for membership testing and set operations.
- **How to iterate into a set**: Use `for element in my_set:` to iterate over elements

### Dictionaries

- **What are dictionaries**: Key-value pairs, also known as hash maps or associative arrays
- **How to use them**: Create with `dict()` or `{key: value}` syntax, access values with `dict[key]`
- **When to use dictionaries vs lists or sets**: Use dictionaries when you need to associate values with unique keys. Faster lookups than lists, more flexible than sets.
- **What is a key in a dictionary**: Keys must be immutable (strings, numbers, tuples), unique within the dictionary
- **How to iterate over a dictionary**:
  - `for key in my_dict:` - iterate over keys
  - `for value in my_dict.values():` - iterate over values
  - `for key, value in my_dict.items():` - iterate over key-value pairs

### Lambda Functions

- **What is a lambda function**: Anonymous, inline functions defined with `lambda` keyword
- **Syntax**: `lambda arguments: expression`
- **Use cases**: Short functions for map, filter, reduce, or as arguments to higher-order functions

### Map, Filter, and Reduce Functions

- **Map**: `map(function, iterable)` - applies function to each element, returns iterator
- **Filter**: `filter(function, iterable)` - filters elements where function returns True
- **Reduce**: `functools.reduce(function, iterable)` - reduces iterable to single value by applying function cumulatively
