# Python - Test-Driven Development

## Repository Overview

This repository introduces the fundamentals of Python test-driven development (TDD). It is designed for learners who want to understand why testing matters, how to write tests, and how to document Python code clearly.

## Learning Objectives

- Understand what an interactive test is
- Learn why tests are important in software development
- Write docstrings that support test creation
- Document modules and functions clearly
- Use basic `pytest` option flags for running tests
- Identify and handle edge cases in test design

## What is an Interactive Test?

An interactive test is a test executed in a way that lets you observe results and behavior immediately. In Python, this often means running test code in a console or using tools like `pytest` to execute tests and inspect the output. Interactive testing helps you verify behavior while developing and iterating quickly.

## Why Tests Are Important

Tests are important because they:

- Verify that code works as expected
- Catch regressions early when code changes
- Encourage better design and modular code
- Provide confidence for refactoring and future updates
- Serve as executable documentation for behavior

## How to Write Docstrings to Create Tests

Docstrings describe expected behavior, inputs, and outputs. They help you design tests by clarifying what each function should do.

Example:

```python
def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int): first integer.
        b (int): second integer, defaults to 98.

    Returns:
        int: the sum of a and b.
    """
    return a + b
```

A well-written docstring makes it easier to create tests that validate:

- correct outputs for normal inputs
- expected error handling
- behavior across edge cases

## How to Write Documentation for Each Module and Function

Good documentation includes a module summary and function details.

- Module docstring: describe the module's purpose
- Function docstring: describe what the function does, parameters, return values, and any exceptions raised
- Keep docstrings concise and informative

Example module header:

```python
"""Utility functions for integer operations.

This module contains helper functions used to validate and add integers.
"""
```

## Basic `pytest` Option Flags

Use these common flags when running tests:

- `pytest`: run all tests in the current directory
- `pytest -q`: quiet mode, minimal output
- `pytest -v`: verbose mode, detailed output
- `pytest tests/test_file.py`: run a specific test file
- `pytest -k "expression"`: run tests matching an expression

These flags help you focus test execution and inspect results efficiently.

## How to Find Edge Cases

Edge cases are unusual or extreme situations where code may fail.

To find them:

- review input types and ranges
- consider empty inputs and missing values
- test boundary values (minimum, maximum)
- think about invalid input and error conditions
- use unexpected input combinations

Example edge cases for an integer addition function:

- non-integer inputs
- very large integers
- integer and float mixing
- missing second argument

## Getting Started

1. Read the module and function docstrings.
2. Write tests that cover normal cases and edge cases.
3. Run `pytest` and update code until tests pass.
4. Keep documentation aligned with actual behavior.
