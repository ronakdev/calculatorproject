#!/usr/bin/python
# Stores my classes until I figure out a better way to store classes in python

class Calculator():

	def __init__ (self):

		self.curr = 0

	def add(self, amt):
		self.curr += amt

	def getValue(self):
		return self.curr
