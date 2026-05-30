#!/usr/bin/python3
"""This module is to override methods of list"""


class VerboseList(list):
    """List that prints notifications on append/extend/remove/pop."""

    def append(self, item):
        """Appends item and announces it"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """extends list with items and annouces it"""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items")

    def remove(self, value):
        """Removes item from list and annouces it"""
        if value in self:
            print(f"Removed [{value}] from the list.")
            super().remove(value)
        else:
            raise ValueError(f"[{value}] not found in list")

    def pop(self, index=-1):
        """Pop item from list and announce it; return the popped item."""
        try:
            item = self[index]
        except IndexError:
            if len(self) == 0:
                raise IndexError("pop from empty list")
            raise IndexError("pop index out of range")
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
