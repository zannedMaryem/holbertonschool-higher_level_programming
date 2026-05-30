#!/usr/bin/python3
"""This module provides a counted iterator class."""


class CountedIterator:
    """Iterator wrapper that counts items consumed."""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the current value of the counter."""
        return self.count
