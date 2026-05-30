#!/usr/bin/python3
"""FlyingFish example demonstrating multiple inheritance and MRO."""


class Fish:
	"""Simple Fish class with swim and habitat behaviors."""

	def swim(self):
		print("The fish is swimming")

	def habitat(self):
		print("The fish lives in water")


class Bird:
	"""Simple Bird class with fly and habitat behaviors."""

	def fly(self):
		print("The bird is flying")

	def habitat(self):
		print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
	"""A creature that inherits from both Fish and Bird.

	Overrides behaviors from both parents to demonstrate multiple
	inheritance and method resolution order (MRO).
	"""

	def fly(self):
		print("The flying fish is soaring!")

	def swim(self):
		print("The flying fish is swimming!")

	def habitat(self):
		print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
	ff = FlyingFish()
	ff.fly()
	ff.swim()
	ff.habitat()
	# Show method resolution order
	print(FlyingFish.mro())
