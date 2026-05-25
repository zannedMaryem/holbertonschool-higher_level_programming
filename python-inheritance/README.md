# Python Inheritance

This README explains the basics of inheritance in Python and introduces the built-in functions used to inspect class relationships.

## Objectives

- Understand what a superclass, base class, and parent class are.
- Understand what a subclass is.
- Learn how to list all attributes and methods of a class or instance.
- Know when an instance can get new attributes.
- Learn how to inherit from another class.
- Learn how to define a class with multiple base classes.
- Know the default class every class inherits from.
- Learn how to override a method or attribute inherited from a base class.
- Understand which attributes and methods are available by inheritance to subclasses.
- Understand the purpose of inheritance.
- Learn how and when to use `isinstance`, `issubclass`, `type`, and `super`.

## 1. What is inheritance?

Inheritance is a mechanism that allows one class to reuse the code and behavior of another class.

A class that provides attributes and methods is called:

- a **superclass**
- a **base class**
- a **parent class**

A class that takes those attributes and methods from another class is called:

- a **subclass**
- a **derived class**
- a **child class**

### Example

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    pass

my_dog = Dog("Rex")
print(my_dog.name)      # Rex
print(my_dog.speak())   # ...
```

## 2. What is a subclass?

A subclass is a class that inherits from another class. It can use the parent's methods and attributes, and it can also add new ones or change inherited behavior.

## 3. How to list all attributes and methods of a class or instance

Python provides `dir()` to list the attributes and methods of an object.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
print(dir(Rectangle))
print(dir(r))
```

A practical example for this repository is the `lookup` function:

```python
def lookup(obj):
    return dir(obj)
```

This returns all public attributes and methods available on the object.

## 4. When can an instance have new attributes?

An instance can always get new attributes unless the class defines `__slots__`.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
p.age = 25
print(p.age)  # 25
```

If a class uses `__slots__`, you restrict which attributes can be added.

## 5. How to inherit from another class

Use the parent class inside parentheses when defining the subclass.

```python
class Parent:
    def method(self):
        return "Parent method"

class Child(Parent):
    pass

obj = Child()
print(obj.method())
```

The subclass automatically inherits the parent’s methods and attributes.

## 6. How to define a class with multiple base classes

Python supports multiple inheritance: a class can inherit from more than one base class.

```python
class A:
    def method_a(self):
        return "A"

class B:
    def method_b(self):
        return "B"

class C(A, B):
    pass

obj = C()
print(obj.method_a())
print(obj.method_b())
```

When methods are inherited from multiple bases, Python uses the order of the base classes.

## 7. What is the default class every class inherits from

Every class in Python inherits from `object` by default, unless another base class is specified.

```python
class MyClass:
    pass

print(MyClass.__bases__)
```

`MyClass.__bases__` will show `(object,)`.

## 8. How to override a method or attribute inherited from the base class

A subclass can redefine a method or attribute from the parent.

```python
class Parent:
    def show(self):
        return "Parent"

class Child(Parent):
    def show(self):
        return "Child"

obj = Child()
print(obj.show())  # Child
```

You can also override an attribute by assigning a new value in the subclass.

## 9. Which attributes or methods are available by heritage to subclasses

All public attributes and methods defined in the parent class are available to the subclass, unless they are hidden by an override.

This includes:

- instance attributes initialized in the parent
- methods defined in the parent
- inherited class methods from the parent’s base classes

Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Sound"

class Cat(Animal):
    pass

c = Cat("Milo")
print(c.name)
print(c.speak())
```

## 10. What is the purpose of inheritance

Inheritance is used to:

- reuse code
- reduce duplication
- organize classes in a logical hierarchy
- make it easier to extend behavior
- create specialized versions of existing classes

For example, `Dog` and `Cat` can both inherit from `Animal` and share common behavior while keeping their own specialization.

## 11. `isinstance`, `issubclass`, `type`, and `super`

### `isinstance(obj, Class)`

Checks whether an object is an instance of a class or of a subclass of that class.

```python
class Animal:
    pass

class Dog(Animal):
    pass

my_dog = Dog()
print(isinstance(my_dog, Dog))   # True
print(isinstance(my_dog, Animal))  # True
```

### `issubclass(SubClass, BaseClass)`

Checks whether one class is a subclass of another.

```python
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
```

### `type(obj)`

Returns the exact type of an object, not considering inheritance.

```python
class Animal:
    pass

class Dog(Animal):
    pass

my_dog = Dog()
print(type(my_dog))  # <class '__main__.Dog'>
```

### `super()`

`super()` allows a subclass to call methods from its parent class.

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

obj = Child("Alice", 12)
print(obj.name)  # Alice
print(obj.age)   # 12
```

`super()` is especially useful when the subclass wants to reuse the parent’s initialization logic.
