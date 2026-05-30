#!/usr/bin/python3
"""Dragon class demonstrating multiple mixins."""


class SwimMixin:
    """Mixin that provides swimming ability."""

    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability."""

    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can both swim and fly."""

    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
