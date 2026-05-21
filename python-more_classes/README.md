# Python Classes and Objects - A Comprehensive Guide

## Table of Contents

1. [What is OOP](#what-is-oop)
2. [First-Class Everything](#first-class-everything)
3. [What is a Class](#what-is-a-class)
4. [What is an Object and an Instance](#what-is-an-object-and-an-instance)
5. [Class vs Object/Instance](#class-vs-objectinstance)
6. [Attributes](#attributes)
7. [Public, Protected, and Private Attributes](#public-protected-and-private-attributes)
8. [Self](#self)
9. [Methods](#methods)
10. [The __init__ Method](#the-__init__-method)
11. [Data Abstraction, Encapsulation, and Information Hiding](#data-abstraction-encapsulation-and-information-hiding)
12. [Properties](#properties)
13. [Attributes vs Properties](#attributes-vs-properties)
14. [Pythonic Getters and Setters](#pythonic-getters-and-setters)
15. [__str__ and __repr__ Methods](#__str__-and-__repr__-methods)
16. [Difference Between __str__ and __repr__](#difference-between-__str__-and-__repr__)
17. [Class Attributes](#class-attributes)
18. [Object vs Class Attributes](#object-vs-class-attributes)
19. [Class Methods](#class-methods)
20. [Static Methods](#static-methods)
21. [Dynamic Attributes](#dynamic-attributes)
22. [Binding Attributes](#binding-attributes)
23. [__dict__ Attribute](#__dict__-attribute)
24. [Attribute Lookup](#attribute-lookup)
25. [getattr Function](#getattr-function)

---

## What is OOP?

__Object-Oriented Programming (OOP)__ is a programming paradigm that uses objects and classes to structure code. It provides a way to:

- __Organize code__ around real-world entities
- __Reuse code__ through inheritance
- __Hide complexity__ through encapsulation
- __Extend functionality__ through polymorphism

### Key Principles

- __Encapsulation__: Bundling data and methods together
- __Inheritance__: Creating hierarchies of classes
- __Polymorphism__: Using methods that behave differently based on the object
- __Abstraction__: Hiding implementation details

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```

---

## First-Class Everything

In Python, __everything is an object__ - including classes themselves! This means:

- Functions, classes, strings, numbers, etc. are all objects
- Classes can be assigned to variables
- Classes can be passed as arguments
- Classes can be returned from functions
- Classes can be stored in data structures

```python
# Functions as first-class objects
def greet():
    return "Hello!"

func = greet  # Assign function to variable
print(func())  # Output: Hello!

# Classes as first-class objects
class MyClass:
    pass

cls = MyClass  # Assign class to variable
obj = cls()    # Create instance using the variable

# Functions can return classes
def create_class(name):
    return type(name, (), {})

DynamicClass = create_class('MyDynamicClass')
```

---

## What is a Class?

A __class__ is a __blueprint or template__ for creating objects. It defines:

- __Attributes__: The data/properties an object will have
- __Methods__: The behaviors/functions an object can perform

Think of a class like a recipe - it defines the ingredients and instructions, but it's not the actual dish itself.

```python
class Car:
    # Class definition
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"{self.brand} {self.model}"

# The class itself is just a template
print(Car)  # <class '__main__.Car'>
```

---

## What is an Object and an Instance?

An __object__ (or __instance__) is a __concrete realization__ of a class. It's created from the class blueprint and has actual data values.

- __Object/Instance__: A specific occurrence of a class
- Each instance has its own copy of attributes
- Created using the class name followed by parentheses

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances (objects)
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name)  # Output: Alice
print(person2.name)  # Output: Bob

# Each instance is a separate object
print(person1 is person2)  # Output: False
print(type(person1))       # <class '__main__.Person'>
```

---

## Class vs Object/Instance

| Aspect | Class | Object/Instance |
|--------|-------|-----------------|
| __Definition__ | Blueprint or template | Actual entity created from the blueprint |
| __Nature__ | Abstract | Concrete |
| __Memory__ | Exists once in memory | Each instance has its own memory space |
| __Data__ | Defines structure | Contains actual data |
| __Example__ | Cookie cutter | Actual cookie |

```python
class Cookie:
    def __init__(self, flavor):
        self.flavor = flavor

# Class: Cookie (template)
# Instances:
chocolate_chip = Cookie("Chocolate Chip")
oatmeal = Cookie("Oatmeal")
sugar = Cookie("Sugar")

# Each instance has its own flavor value
```

---

## Attributes

An __attribute__ is a __variable__ that belongs to a class or instance. It stores data/state about the object.

### Types of Attributes

1. __Instance Attributes__: Belong to specific instances
2. __Class Attributes__: Belong to the class itself, shared by all instances

```python
class Person:
    species = "Homo sapiens"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute

person = Person("Alice")
print(person.name)           # Instance attribute
print(Person.species)        # Class attribute
print(person.species)        # Can access class attributes from instances
```

---

## Public, Protected, and Private Attributes

Python uses naming conventions to indicate the intended accessibility of attributes:

### 1. Public Attributes

- __Convention__: No leading underscores
- __Access__: Can be accessed from anywhere
- __Usage__: For data that should be freely available

```python
class BankAccount:
    def __init__(self, owner):
        self.owner = owner  # Public attribute
        self.balance = 0    # Public attribute
```

### 2. Protected Attributes

- __Convention__: Single leading underscore `_attribute`
- __Access__: Can be accessed, but signals "internal use"
- __Usage__: For data meant for internal use but subclasses might need access
- __Note__: This is a __convention__, not enforced by Python

```python
class Parent:
    def __init__(self):
        self._protected = "I'm protected"  # Protected attribute

class Child(Parent):
    def access_protected(self):
        return self._protected  # Subclasses can access

obj = Parent()
print(obj._protected)  # Works, but shouldn't be used outside the class
```

### 3. Private Attributes

- __Convention__: Double leading underscore `__attribute`
- __Access__: Name mangling makes it harder to access from outside
- __Usage__: For data that should only be used within the class
- __Note__: Python uses __name mangling__ (not true privacy)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
# print(account.__balance)    # Error: AttributeError
# But Python mangles it to: _BankAccount__balance
print(account._BankAccount__balance)  # Works, but don't do this!
```

### Summary

```python
class Example:
    public = "Everyone can use me"
    _protected = "Use me, but I'm internal"
    __private = "Use methods to access me"
    
    def __init__(self):
        self.public_attr = "public"
        self._protected_attr = "protected"
        self.__private_attr = "private"
```

---

## Self

__`self`__ is a reference to the __instance itself__. It allows methods to:

- Access instance attributes
- Call other methods on the instance
- Modify instance state

__Key Points:__

- `self` is just a __convention__ (could be named anything, but always use `self`)
- The first parameter of any instance method
- Python passes the instance automatically when you call a method
- Use `self.attribute` to access instance attributes

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Use self to set instance attributes
        self.age = age
    
    def greet(self):
        # self refers to the specific instance
        return f"Hello, I'm {self.name}"
    
    def have_birthday(self):
        self.age += 1  # Modify instance attribute through self
        self.greet()   # Call other methods through self

person = Person("Alice", 30)
person.have_birthday()  # Python passes person as self automatically
print(person.age)  # Output: 31
```

__`self` vs `cls`:__

- `self`: Used in instance methods, refers to the instance
- `cls`: Used in class methods, refers to the class

---

## Methods

A __method__ is a __function defined inside a class__ that describes behavior or actions an object can perform. Methods can access and modify instance state.

### Types of Methods

1. __Instance Methods__: Operate on instance data
2. __Class Methods__: Operate on class data
3. __Static Methods__: Don't depend on instance or class data

```python
class Calculator:
    total_operations = 0  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute
    
    # Instance method
    def add(self, a, b):
        self.last_result = a + b
        Calculator.total_operations += 1
        return self.last_result
    
    # Class method
    @classmethod
    def from_name(cls, name):
        return cls(name)
    
    # Static method
    @staticmethod
    def is_positive(num):
        return num > 0

calc = Calculator("MyCalc")
print(calc.add(5, 3))  # Output: 8
print(Calculator.total_operations)  # Output: 1
print(Calculator.is_positive(-5))  # Output: False
```

---

## The __init__ Method

__`__init__`__ is the __constructor/initializer__ method. It's called automatically when a new instance is created.

__Purpose:__

- Initialize instance attributes
- Set up the initial state of the object
- Run setup code

__Key Points:__

- Not required, but highly recommended
- Called before the instance is returned to the caller
- Must have `self` as the first parameter
- Can have additional parameters for initialization data

```python
class Student:
    def __init__(self, name, student_id, gpa=0.0):
        # Initialize instance attributes
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        self.courses = []  # Initialize empty list
    
    def enroll(self, course):
        self.courses.append(course)

# __init__ is called automatically
student = Student("Alice", 12345)
print(student.name)     # Output: Alice
print(student.courses)  # Output: []

student2 = Student("Bob", 12346, 3.8)
print(student2.gpa)  # Output: 3.8
```

__Without `__init__`:__

```python
class Simple:
    pass

obj = Simple()
obj.name = "Manual"  # Must set attributes manually
```

---

## Data Abstraction, Encapsulation, and Information Hiding

### Data Abstraction
__Hiding complexity__ by showing only essential features, not implementation details.

```python
class Car:
    def __init__(self, model):
        self.model = model
        self._engine_status = "off"
    
    def start(self):
        # Abstract away the complex engine startup process
        self._engine_status = "on"
        print(f"{self.model} started")
    
    def stop(self):
        self._engine_status = "off"
        print(f"{self.model} stopped")

car = Car("Tesla")
car.start()  # User doesn't need to know HOW it starts
# Instead of: car.turn_on_battery(); car.ignite_fuel(); etc.
```

### Encapsulation
__Bundling data (attributes) and methods together__ into a single unit (class), and controlling access.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Encapsulated data
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# account.__balance = -9999  # Can't do this directly
```

### Information Hiding
__Restricting access__ to internal details that shouldn't be modified directly.

```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self.__celsius = value

temp = Temperature(0)
print(temp.fahrenheit)  # Output: 32.0
temp.celsius = 25
print(temp.celsius)  # Output: 25
```

---

## Properties

A __property__ is a way to define __getters and setters__ for attributes using decorators. It allows you to use attribute-like syntax while executing custom code.

__Benefits:__

- Validation of data
- Computation of values
- Lazy loading
- Side effects on get/set

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter with validation"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Computed property"""
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.radius)  # Output: 5 (uses getter)
print(circle.area)    # Output: 78.53975 (computed)

circle.radius = 10    # Uses setter
print(circle.area)    # Output: 314.159 (recomputed)

# circle.radius = -5  # Raises ValueError
```

---

## Attributes vs Properties

| Aspect | Attribute | Property |
|--------|-----------|----------|
| __Definition__ | Variable storing data | Computed value using methods |
| __Syntax__ | Direct: `obj.attr` | Looks like attribute: `obj.prop` |
| __Validation__ | None (direct assignment) | Can validate during setter |
| __Computation__ | Just stored data | Can compute on access |
| __Performance__ | Instant | Slightly slower (method call) |
| __Use Case__ | Simple data storage | Complex logic, validation |

```python
class Temperature:
    # Attribute approach
    def __init__(self):
        self.celsius = 0
    
    # User can do: temp.celsius = -9999 (no validation!)

class BetterTemperature:
    def __init__(self):
        self._celsius = 0
    
    # Property approach with validation
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Invalid temperature")
        self._celsius = value

temp = BetterTemperature()
temp.celsius = 25  # Validated automatically
# temp.celsius = -9999  # Raises ValueError
```

---

## Pythonic Getters and Setters

In Python, the __Pythonic way__ is to use __@property decorators__ instead of traditional getter/setter methods (like in Java).

### Traditional (Not Pythonic)

```python
class Person:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value

person = Person("Alice")
print(person.get_name())  # Not Pythonic!
person.set_name("Bob")
```

### Pythonic (Recommended)

```python
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

person = Person("Alice")
print(person.name)   # Pythonic! Looks like attribute access
person.name = "Bob"  # Pythonic! Looks like attribute assignment
# person.name = 123   # Raises TypeError
```

### With Computed Properties

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, value):
        first, last = value.split()
        self.first_name = first
        self.last_name = last

person = Person("John", "Doe")
print(person.full_name)  # Output: John Doe
person.full_name = "Jane Smith"
print(person.first_name)  # Output: Jane
```

---

## __str__ and __repr__ Methods

These are __special methods__ (dunder methods) that define how an object is represented as a string.

### __str__ Method

- __Purpose__: User-friendly, readable string representation
- __Called by__: `str()`, `print()`, `format()`
- __Should return__: A string that's easy for humans to understand

### __repr__ Method

- __Purpose__: Developer-friendly, unambiguous representation
- __Called by__: `repr()`, interactive REPL, debugging
- __Should return__: A string that could ideally recreate the object or show its state

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        # User-friendly representation
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        # Developer-friendly representation
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(str(person))   # Output: Alice is 30 years old
print(repr(person))  # Output: Person(name='Alice', age=30)
print(person)        # Output: Alice is 30 years old (uses __str__)
```

---

## Difference Between __str__ and __repr__

| Aspect | __str__ | __repr__ |
|--------|---------|----------|
| __Purpose__ | Human-readable | Unambiguous, for debugging |
| __Audience__ | End users | Developers |
| __Called by__ | `str()`, `print()` | `repr()`, REPL |
| __Goal__ | Readability | Information completeness |
| __Fallback__ | Uses `__repr__` if not defined | Uses default `<class ...>` |

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        # What a regular user wants to see
        return f'"{self.title}" by {self.author}'
    
    def __repr__(self):
        # What a developer wants to see
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

book = Book("1984", "George Orwell", 328)

# In an interactive Python session:
# >>> book
# Book(title='1984', author='George Orwell', pages=328)  # __repr__

print(book)  # Output: "1984" by George Orwell  # __str__
print(repr(book))  # Output: Book(title='1984', author='George Orwell', pages=328)
```

__Best Practice:__

- Always define `__repr__`
- Define `__str__` if you want a different user-friendly version
- `__repr__` should ideally be executable Python code

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        # Ideally, you could do: Point(*eval(repr(p)))
        return f"Point({self.x}, {self.y})"
```

---

## Class Attributes

A __class attribute__ is a __variable that belongs to the class itself__, not to individual instances. It's __shared by all instances__.

__Key Points:__

- Defined directly in the class body
- Shared by all instances
- Accessed via `ClassName.attribute` or `instance.attribute`
- Good for default values and constants

```python
class Car:
    # Class attributes
    total_cars = 0
    max_speed = 200
    
    def __init__(self, brand):
        self.brand = brand  # Instance attribute
        Car.total_cars += 1  # Increment class attribute
    
    def display_info(self):
        return f"{self.brand} - Max Speed: {Car.max_speed} mph"

car1 = Car("Toyota")
car2 = Car("Honda")

print(Car.total_cars)  # Output: 2 (shared across all instances)
print(car1.total_cars)  # Output: 2 (can access via instance too)
print(car1.display_info())  # Output: Toyota - Max Speed: 200 mph

# Modifying class attribute affects all instances
Car.max_speed = 250
print(car2.display_info())  # Output: Honda - Max Speed: 250 mph
```

---

## Object vs Class Attributes

| Aspect | Object/Instance Attribute | Class Attribute |
|--------|---------------------------|-----------------|
| __Scope__ | Belongs to specific instance | Belongs to the class |
| __Memory__ | Each instance has its own copy | Shared across all instances |
| __Definition__ | In `__init__` using `self.attr` | In class body directly |
| __Access__ | Via `instance.attr` | Via `ClassName.attr` or `instance.attr` |
| __Modification__ | Affects only that instance | Affects all instances |
| __Use Case__ | Store instance-specific data | Store shared data, constants |

```python
class Student:
    school = "High School"  # Class attribute - shared
    
    def __init__(self, name, grade):
        self.name = name      # Instance attribute
        self.grade = grade    # Instance attribute

student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

# Instance attributes are different
print(student1.name, student2.name)  # Output: Alice Bob
print(student1.grade, student2.grade)  # Output: A B

# Class attribute is the same
print(student1.school, student2.school)  # Output: High School High School
print(Student.school)  # Output: High School

# Modifying instance attribute only affects that instance
student1.grade = "A+"
print(student1.grade, student2.grade)  # Output: A+ B

# Modifying class attribute affects all
Student.school = "University"
print(student1.school, student2.school)  # Output: University University
```

---

## Class Methods

A __class method__ is a method that operates on the __class itself__, not on instances. It receives the __class__ as the first parameter (usually named `cls`).

__Key Points:__

- Decorated with `@classmethod`
- First parameter is `cls` (not `self`)
- Can access and modify class attributes
- Can create instances (alternative constructors)
- Called on the class: `ClassName.method()`

```python
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
    
    @classmethod
    def get_population(cls):
        return cls.population
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor"""
        from datetime import datetime
        age = datetime.now().year - birth_year
        return cls(name)
    
    def __repr__(self):
        return f"Person(name='{self.name}')"

# Using class method as constructor
person1 = Person.from_birth_year("Alice", 1990)
person2 = Person("Bob")

print(Person.get_population())  # Output: 2
print(person1)  # Output: Person(name='Alice')
```

### When to Use Class Methods

1. Alternative constructors
2. Modifying class state
3. Factory methods
4. Creating instances from different data formats

```python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_string(cls, date_string):
        """Create instance from 'DD/MM/YYYY' string"""
        day, month, year = map(int, date_string.split('/'))
        return cls(day, month, year)
    
    @classmethod
    def today(cls):
        """Create instance for today's date"""
        from datetime import datetime
        now = datetime.now()
        return cls(now.day, now.month, now.year)

date1 = Date.from_string("15/05/2024")
date2 = Date.today()
```

---

## Static Methods

A __static method__ is a method that __doesn't depend on instance or class data__. It's just a function bundled with the class for organization.

__Key Points:__

- Decorated with `@staticmethod`
- No `self` or `cls` parameter
- Cannot access instance or class attributes directly
- Called on the class or instance: `ClassName.method()` or `instance.method()`
- Useful for utility/helper functions

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * Math.factorial(n - 1)

print(Math.add(5, 3))  # Output: 8
print(Math.is_even(4))  # Output: True
print(Math.factorial(5))  # Output: 120

# Can also call on instance
math_obj = Math()
print(math_obj.add(2, 3))  # Output: 5
```

### Instance Method vs Class Method vs Static Method

```python
class Example:
    class_var = "Class Variable"
    
    def __init__(self, instance_var):
        self.instance_var = instance_var
    
    # Instance method - uses self
    def instance_method(self):
        return f"Instance: {self.instance_var}"
    
    # Class method - uses cls
    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_var}"
    
    # Static method - uses neither
    @staticmethod
    def static_method():
        return "Static"

obj = Example("data")
print(obj.instance_method())  # Output: Instance: data
print(Example.class_method())  # Output: Class: Class Variable
print(Example.static_method())  # Output: Static
```

---

## Dynamic Attributes

You can __add attributes to instances dynamically__ even after the object is created. Python allows adding attributes on the fly.

__Key Points:__

- Attributes don't need to be predefined
- Can be added anytime: `obj.new_attr = value`
- Each instance can have different attributes
- Not recommended for large projects (use `__slots__` or `__init__`)

```python
class DynamicClass:
    def __init__(self, name):
        self.name = name

obj = DynamicClass("Alice")
print(obj.name)  # Output: Alice

# Add attributes dynamically
obj.age = 30
obj.email = "alice@example.com"
obj.score = 95.5

print(obj.age)  # Output: 30
print(obj.email)  # Output: alice@example.com

# Different instances can have different attributes
obj2 = DynamicClass("Bob")
obj2.phone = "555-1234"  # Only obj2 has this attribute

print(hasattr(obj, 'phone'))  # Output: False
print(hasattr(obj2, 'phone'))  # Output: True
```

### Controlling Dynamic Attributes with __slots__

For performance and preventing typos, you can restrict which attributes are allowed:

```python
class RestrictedClass:
    __slots__ = ['name', 'age']  # Only these attributes allowed
    
    def __init__(self, name):
        self.name = name

obj = RestrictedClass("Alice")
obj.age = 30  # OK
# obj.email = "alice@example.com"  # AttributeError!
```

---

## Binding Attributes

__Binding__ means __associating data with a class or instance__. There are different ways to bind attributes:

### Instance Binding

```python
class MyClass:
    pass

obj = MyClass()
obj.name = "Instance attribute"  # Bind attribute to instance
```

### Class Binding

```python
class MyClass:
    pass

MyClass.class_attr = "Class attribute"  # Bind attribute to class
```

### Method Binding

Methods are bound when accessed through an instance:

```python
class MyClass:
    def method(self):
        return "Method"

obj = MyClass()
bound_method = obj.method  # Method is bound to obj
unbound_method = MyClass.method  # Function, not bound

print(bound_method())  # Output: Method
print(unbound_method(obj))  # Must pass instance explicitly
```

### Binding Example

```python
def external_func(self):
    return f"External function: {self.name}"

class MyClass:
    def __init__(self, name):
        self.name = name

# Bind function to class
MyClass.new_method = external_func

obj = MyClass("Alice")
print(obj.new_method())  # Output: External function: Alice
```

---

## __dict__ Attribute

__`__dict__`__ is a dictionary that stores an object's or class's attributes.

### Instance __dict__

Contains all instance attributes:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.__dict__)  # Output: {'name': 'Alice', 'age': 30}

# Can modify via __dict__
person.__dict__['email'] = "alice@example.com"
print(person.email)  # Output: alice@example.com

# Can iterate over attributes
for key, value in person.__dict__.items():
    print(f"{key}: {value}")
```

### Class __dict__

Contains class attributes, methods, and special attributes:

```python
class MyClass:
    class_var = 10
    
    def __init__(self):
        self.instance_var = 20
    
    def method(self):
        pass

print(MyClass.__dict__)
# Output includes: 'class_var', '__init__', 'method', etc.

# Methods are also in __dict__
print(type(MyClass.__dict__['method']))  # <class 'function'>
print(type(MyClass.__dict__['__init__']))  # <class 'function'>
```

### Comparing Instance and Class __dict__

```python
class Person:
    species = "Homo sapiens"
    
    def __init__(self, name):
        self.name = name

person = Person("Alice")

# Instance __dict__ - only instance attributes
print(person.__dict__)  # Output: {'name': 'Alice'}

# Class __dict__ - class attributes, methods, special attributes
print("species" in Person.__dict__)  # Output: True
print("name" in Person.__dict__)  # Output: False (it's in instance __dict__)
print("species" in person.__dict__)  # Output: False
```

---

## Attribute Lookup

Python uses a specific __order to search for attributes__:

### Lookup Order (Method Resolution Order - MRO)

1. __Instance __dict____: Instance attributes
2. __Class __dict____: Class attributes and methods
3. __Parent classes__: If inheritance is used (follows MRO)
4. __AttributeError__: If not found anywhere

```python
class MyClass:
    class_attr = "I'm in class"
    
    def __init__(self):
        self.instance_attr = "I'm in instance"

obj = MyClass()

# Instance attribute lookup
print(obj.instance_attr)  # Found in obj.__dict__

# Class attribute lookup
print(obj.class_attr)  # Not in obj.__dict__, found in MyClass.__dict__

# Attribute not found
try:
    print(obj.nonexistent)  # AttributeError
except AttributeError:
    print("Attribute not found")
```

### Lookup with Inheritance

```python
class Parent:
    parent_attr = "Parent"

class Child(Parent):
    child_attr = "Child"

obj = Child()
print(obj.parent_attr)  # Found in Parent class (via inheritance)
print(obj.child_attr)   # Found in Child class
```

### Viewing MRO

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())  # Shows the method resolution order
# Output: [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]

# Or use:
print(D.__mro__)  # Same as .mro()
```

---

## getattr Function

__`getattr()`__ is a built-in function that __gets an attribute value__ from an object. It's useful for:

- Getting attributes dynamically
- Providing default values if attribute doesn't exist
- Avoiding AttributeError

### Syntax

```python
getattr(object, name)              # No default
getattr(object, name, default)     # With default value
```

### Examples

#### Basic Usage

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

# Standard attribute access
print(person.name)  # Output: Alice

# Using getattr - equivalent to above
print(getattr(person, 'name'))  # Output: Alice
```

#### With Default Value

```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")

# Standard way - raises AttributeError
try:
    print(person.age)  # AttributeError
except AttributeError:
    print("age not found")

# Using getattr with default - no error
print(getattr(person, 'age', 'Not specified'))  # Output: Not specified
```

#### Dynamic Attribute Access

```python
class Config:
    def __init__(self):
        self.database = "localhost"
        self.port = 5432
        self.timeout = 30

config = Config()

# Get attributes dynamically
attrs = ['database', 'port', 'timeout']
for attr in attrs:
    value = getattr(config, attr)
    print(f"{attr}: {value}")

# With method calls
class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

calc = Calculator()

# Call methods dynamically
method_name = 'add'
method = getattr(calc, method_name)
print(method(5, 3))  # Output: 8
```

#### Getting Methods

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person("Alice")

# Get method using getattr
method = getattr(person, 'greet')
print(method())  # Output: Hello, I'm Alice

# Check if method exists before calling
if hasattr(person, 'greet'):
    getattr(person, 'greet')()
```

#### Conditional Attribute Access

```python
class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        if is_admin:
            self.admin_level = 5

user = User("Alice", is_admin=True)
print(getattr(user, 'admin_level', 0))  # Output: 5

user2 = User("Bob")
print(getattr(user2, 'admin_level', 0))  # Output: 0 (default)
```

### getattr with callable()

```python
class MyClass:
    def method(self):
        return "Method"
    
    def __init__(self):
        self.attribute = "Attribute"

obj = MyClass()

# Check if it's callable
item = getattr(obj, 'method')
if callable(item):
    print(item())  # Output: Method

item = getattr(obj, 'attribute')
if callable(item):
    print(item())
else:
    print(f"Value: {item}")  # Output: Value: Attribute
```

---

## Summary Table

| Concept | Purpose | Example |
|---------|---------|---------|
| __Class__ | Blueprint for objects | `class Dog: ...` |
| __Instance__ | Concrete object from class | `my_dog = Dog()` |
| __Attribute__ | Variable in class/instance | `self.name = "Buddy"` |
| __Method__ | Function in class | `def bark(self): ...` |
| ____init____ | Constructor/initializer | `def __init__(self): ...` |
| __self__ | Reference to instance | Used in all instance methods |
| __@property__ | Attribute with logic | `@property def age(self): ...` |
| __@classmethod__ | Method on class, not instance | `@classmethod def count(cls): ...` |
| __@staticmethod__ | Function in class | `@staticmethod def helper(): ...` |
| ____str____ | User-friendly string | Return readable string |
| ____repr____ | Developer-friendly string | Return exact representation |
| __Class attribute__ | Shared by all instances | `total = 0` |
| __Instance attribute__ | Unique per instance | `self.id = 1` |
| ____dict____ | Dictionary of attributes | Access all attributes as dict |
| __getattr()__ | Get attribute dynamically | `getattr(obj, 'name', default)` |

---

## Best Practices

1. __Always use `@property` for getters/setters__ - More Pythonic than `get_` and `set_` methods
2. __Use `__init__` to initialize__ - Set up initial state properly
3. __Use `__repr__` always, `__str__` when useful__ - Better debugging and readability
4. __Protect with `_protected` or `__private`__ - Signal intent, though Python has no true privacy
5. __Use class methods for alternative constructors__ - More readable than factory functions
6. __Use static methods for utility functions__ - Keeps related code together
7. __Use `getattr()` for dynamic access__ - Safer than assuming attribute exists
8. __Document with docstrings__ - Explain what your classes and methods do
9. __Follow naming conventions__ - Makes code intent clear
10. __Test your classes thoroughly__ - OOP code can have complex interactions

---

## Additional Resources

- Read Python documentation on classes and objects
- Practice writing classes for real-world entities
- Study existing code and how they structure their classes
- Learn about inheritance and polymorphism next
- Experiment with `__dict__`, `getattr()`, and other introspection tools
