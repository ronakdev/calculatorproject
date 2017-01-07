#!/usr/bin/python
# Stores my classes until I figure out a better way to store classes in python

class Calculator():

	def __init__ (self):

		self.curr = 0
		self.left = 0

	def clear(self):
		self.curr = 0

	#Add as in add a number to the existing number
	def add(self, value):
		self.curr = value if self.curr == 0 else int(str(self.curr) + str(value))
	
	def getValue(self):
		return self.curr

	def operate(self, operator):
		self.left = self.curr
		self.curr = 0
		self.operator = operator

	def evaluate(self):
		v = self.eval()
		self.curr = v
		return v

	def eval(self):
		if (self.operator == "+"):
			return self.left + self.curr
		elif (self.operator == "-"):
			return self.left - self.curr
		elif (self.operator == "*"):
					return self.left * self.curr
		elif (self.operator == "/"):
					return self.left / self.curr

		return "wtf happened"

