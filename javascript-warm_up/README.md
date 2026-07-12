# JavaScript Basics Learning Guide

This document is a practical introduction to JavaScript fundamentals. Each section includes a small code example and a short explanation of why the example is useful.

## 1. Why JavaScript programming is amazing

JavaScript is powerful because it can run in the browser, on servers, and in many modern applications. It is one of the most common languages for building interactive websites and web apps.

```javascript
console.log("JavaScript is amazing!");
```

Commentary: This simple line demonstrates how JavaScript can immediately display output and help you verify that your code is running.

## 2. How to run a JavaScript script

You can run JavaScript with Node.js from the terminal.

```bash
node 0-javascript_is_amazing.js
```

Commentary: Running a script from the terminal is the easiest way to test and debug your code.

## 3. How to create variables and constants

Use variables to store values that may change and constants for values that should stay fixed.

```javascript
let name = "Alice";
const PI = 3.14;

console.log(name);
console.log(PI);
```

Commentary: The example shows how variables and constants are declared and printed to the console.

## 4. Differences between var, const and let

- `var` is function-scoped and can be redeclared.
- `let` is block-scoped and can be reassigned.
- `const` is block-scoped and cannot be reassigned.

```javascript
var age = 20;
let score = 100;
const MAX = 10;

age = 21;
score = 101;
// MAX = 11; // This would cause an error

console.log(age, score, MAX);
```

Commentary: This example helps you understand how each declaration behaves in real code.

## 5. All the data types available in JavaScript

JavaScript has primitive and reference types.

```javascript
let text = "Hello";      // string
let number = 42;         // number
let isReady = true;      // boolean
let emptyValue = null;   // null
let undefinedValue;      // undefined
let id = Symbol("id");  // symbol
let person = { name: "Bob" }; // object

console.log(typeof text);
console.log(typeof number);
console.log(typeof isReady);
console.log(typeof emptyValue);
console.log(typeof undefinedValue);
console.log(typeof id);
console.log(typeof person);
```

Commentary: Understanding data types helps you choose the right structure for your values.

## 6. How to use if and if...else statements

Conditionals let your program make decisions.

```javascript
let age = 18;

if (age >= 18) {
  console.log("You are an adult.");
} else {
  console.log("You are a minor.");
}
```

Commentary: This code shows how a program can respond differently depending on a condition.

## 7. How to use comments

Comments explain code and make it easier to read.

```javascript
// This is a single-line comment

/*
This is a
multi-line comment
*/

let message = "Comments help developers";
console.log(message);
```

Commentary: Comments are useful for explaining intent without changing program behavior.

## 8. How to affect values to variables

The assignment operator `=` gives a value to a variable.

```javascript
let firstName = "Mina";
let lastName = "Khan";
let fullName = firstName + " " + lastName;

console.log(fullName);
```

Commentary: This example demonstrates how values are stored and combined into new values.

## 9. How to use while and for loops

Loops repeat actions until a condition changes or a fixed number of iterations is reached.

```javascript
let count = 0;

while (count < 3) {
  console.log("While loop:", count);
  count++;
}

for (let i = 0; i < 3; i++) {
  console.log("For loop:", i);
}
```

Commentary: Loops save time when you need to repeat the same action several times.

## 10. How to use break and continue statements

Use `break` to stop a loop and `continue` to skip the current iteration.

```javascript
for (let i = 0; i < 6; i++) {
  if (i === 3) {
    break;
  }

  if (i === 1) {
    continue;
  }

  console.log(i);
}
```

Commentary: These statements give you more control over loop behavior.

## 11. What is a function and how do you use functions

A function groups code into a reusable block.

```javascript
function greet(name) {
  return "Hello, " + name;
}

console.log(greet("Sara"));
```

Commentary: Functions make code easier to organize and reuse.

## 12. What does a function that does not use any return statement return

If a function does not return a value, it returns `undefined`.

```javascript
function showMessage() {
  console.log("This function has no return value.");
}

let result = showMessage();
console.log(result);
```

Commentary: This example shows that a function without an explicit return produces `undefined`.

## 13. Scope of variables

Scope defines where a variable can be used.

```javascript
let globalValue = "I am global";

function testScope() {
  let localValue = "I am local";
  console.log(globalValue);
  console.log(localValue);
}

testScope();
// console.log(localValue); // This would cause an error
```

Commentary: Scope helps prevent accidental changes to variables in the wrong part of the program.

## 14. Arithmetic operators and how to use them

JavaScript uses operators such as `+`, `-`, `*`, `/`, `%`, and `**`.

```javascript
let a = 10;
let b = 3;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);
console.log(a ** b);
```

Commentary: Arithmetic operators are the basic tools for calculations in JavaScript.

## 15. How to manipulate a dictionary

In JavaScript, objects are often used as dictionaries or key-value stores.

```javascript
let user = {
  firstName: "Leo",
  lastName: "Martin",
  age: 25
};

console.log(user.firstName);
console.log(user["lastName"]);

user.age = 26;
user.city = "Paris";

console.log(user);
```

Commentary: Objects are useful for storing related pieces of information together.

## 16. How to import a file

You can split code into multiple files and import them.

### File: math.js

```javascript
function add(a, b) {
  return a + b;
}

module.exports = { add };
```

### File: app.js

```javascript
const math = require("./math");

console.log(math.add(2, 3));
```

Commentary: Importing files helps organize larger programs into smaller, maintainable modules.

## Summary

These concepts form the foundation of JavaScript programming. Once you understand variables, conditionals, loops, functions, and objects, you can build more advanced applications with confidence.
