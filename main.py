#!/usr/bin/python

#from Calculator import *
import core

calc = core.Calculator()

while True:
	a = raw_input()
	if a == "c":
		calc.clear()
	else:
		calc.add(a)
	print(calc.getValue())

