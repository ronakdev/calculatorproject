#!/usr/bin/python
# Stores my classes until I figure out a better way to store classes in python

class Calculator():

	def __init__ (self):

		self.curr = 0

	def clear(self):
		self.curr = 0

	#Add as in add a number to the existing number
	def add(self, value):
		self.curr = value if self.curr == 0 else int(str(self.curr) + str(value))
	def getValue(self):
		return self.curr
