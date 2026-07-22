# JavaScript DOM Manipulation

## Objective

The goal of this guide is to help you learn how to work with the Document Object Model (DOM) using JavaScript. By the end of this tutorial, you should be able to select elements, change their styles and content, update the page structure, make requests, and respond to user interactions.

## Learning goals

By studying this guide, you will learn how to:

- select HTML elements in JavaScript
- understand the difference between ID, class, and tag selectors
- modify an element's style
- get and update element content
- change the DOM structure
- make requests with XMLHttpRequest and Fetch API
- listen to DOM and user events

---

## 1. How to select HTML elements in JavaScript

You can access elements in the page using the document object. Common methods are:

- `getElementById()` for a single element with an ID
- `querySelector()` for the first matching element
- `querySelectorAll()` for all matching elements
- `getElementsByClassName()` for elements with the same class
- `getElementsByTagName()` for elements with the same tag name

```html
<div id="title">Hello World</div>
<p class="message">This is a paragraph.</p>
<ul>
  <li>First item</li>
  <li>Second item</li>
</ul>
```

```javascript
// Select one element by its ID
const title = document.getElementById('title');
console.log(title.textContent);

// Select the first element that matches a CSS selector
const message = document.querySelector('.message');
console.log(message.textContent);

// Select all list items
const items = document.querySelectorAll('li');
items.forEach((item) => console.log(item.textContent));
```

## 2. Differences between ID, class, and tag name selectors

Here is the main difference between the selectors:

- ID selector: targets one unique element. Use it for a single specific element.
- Class selector: targets one or many elements that share the same class.
- Tag name selector: targets all elements of the same HTML tag, such as `p`, `div`, or `li`.

```html
<div id="main-box" class="box"></div>
<div class="box"></div>
<p>Paragraph 1</p>
<p>Paragraph 2</p>
```

```javascript
// ID selector: returns one unique element
const mainBox = document.getElementById('main-box');

// Class selector: returns all elements with the class "box"
const boxes = document.getElementsByClassName('box');
console.log(boxes.length);

// Tag selector: returns all paragraph elements
const paragraphs = document.getElementsByTagName('p');
console.log(paragraphs.length);
```

## 3. How to modify an HTML element style

You can change the appearance of an element by using the `style` property.

```html
<button id="button">Click me</button>
```

```javascript
const button = document.getElementById('button');

// Change the style directly
button.style.backgroundColor = 'blue';
button.style.color = 'white';
button.style.padding = '10px';
```

## 4. How to get and update an HTML element content

You can read or change the content of an element with `textContent` or `innerHTML`.

```html
<h2 id="heading">Original title</h2>
```

```javascript
const heading = document.getElementById('heading');

// Read the current text
console.log(heading.textContent);

// Update the text content
heading.textContent = 'Updated title';

// Use innerHTML if you want to insert HTML
// Note: be careful because it can allow unsafe code
heading.innerHTML = '<strong>Updated with HTML</strong>';
```

## 5. How to modify the DOM

The DOM can be changed by creating new elements and inserting them into the page.

```html
<ul id="list"></ul>
```

```javascript
const list = document.getElementById('list');

// Create a new list item
const item = document.createElement('li');
item.textContent = 'New item';

// Add the new item to the list
list.appendChild(item);

// Remove the first child if it exists
if (list.firstChild) {
  list.removeChild(list.firstChild);
}
```

## 6. How to make a request with XMLHttpRequest

`XMLHttpRequest` is an older way to make HTTP requests from JavaScript.

```javascript
const xhr = new XMLHttpRequest();

xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts/1');

xhr.onload = function () {
  if (xhr.status === 200) {
    console.log('Response received:', xhr.responseText);
  } else {
    console.log('Request failed');
  }
};

xhr.onerror = function () {
  console.log('Network error');
};

xhr.send();
```

## 7. How to make a request with the Fetch API

The Fetch API is the modern way to make HTTP requests.

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then((data) => {
    console.log('Fetched data:', data);
  })
  .catch((error) => {
    console.log('Error:', error);
  });
```

## 8. How to listen and bind to DOM events

Events allow your script to react when the user interacts with the page.

```html
<button id="demo-btn">Press me</button>
```

```javascript
const demoButton = document.getElementById('demo-btn');

// Add a click event listener
// This function runs when the button is clicked
demoButton.addEventListener('click', function () {
  alert('Button clicked!');
});
```

## 9. How to listen and bind to user events

User events include actions such as typing, pressing keys, or moving the mouse.

```html
<input id="name-input" type="text" placeholder="Type your name" />
```

```javascript
const input = document.getElementById('name-input');

// Run code when the user types in the input field
input.addEventListener('input', function (event) {
  console.log('User typed:', event.target.value);
});

// Run code when the user presses a key
input.addEventListener('keydown', function (event) {
  if (event.key === 'Enter') {
    console.log('Enter key pressed');
  }
});
```

## Practice exercises

Try these small challenges to strengthen your understanding:

1. Create a button that changes the text of a heading when clicked.
2. Change the background color of a paragraph using JavaScript.
3. Add a new list item to an unordered list when a user clicks a button.
4. Use Fetch API to display data from a public API on the page.
5. Build a simple form that shows the typed value in real time.

## Summary

Learning DOM manipulation helps you build interactive web pages by:

- selecting elements
- changing their style and content
- adding or removing elements from the page
- sending requests to servers
- reacting to user actions

Practice these examples in a browser to understand how JavaScript changes the DOM in real time.
