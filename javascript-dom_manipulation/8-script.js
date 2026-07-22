#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').innerText = data.hello;
    })
    .catch(error => console.error('Error:', error));
});
