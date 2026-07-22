#!/usr/bin/node
document.querySelector('#update_header').addEventListener('click', function () {
  document.querySelector('header').innerText = 'New Header!!!';
});
