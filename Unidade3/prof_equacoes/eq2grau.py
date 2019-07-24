#coding: utf-8

import math

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

delta = ((b ** 2) - (4 * a * c))
d = delta

if delta < 0:
	delta = delta * (-1)
	
x1 = float(((-1 * b) + (math.sqrt(delta))) / (2 * a))
x2 = float(((-1 * b) - (math.sqrt(delta))) / (2 * a))

if d < 0:
	print "sem raizes reais"

elif (x1 > 0 or x1 < 0) and (x2 > 0 or x2 < 0) and (x1 == x2):
	print "x = %.2f" % x1

elif (x1 > 0 or x1 < 0) and (x2 > 0 or x2 < 0):
	print "x1 = %.2f" % x1
	print "x2 = %.2f" % x2
	
elif (x1 > 0 or x1 < 0) and (x2 == 0):
	print "x = %.2f" % x1
	
elif (x2 > 0 or x2 < 0) and (x1 == 0):
	print "x = %.2f" % x2
	
else:
	print "sem raizes reais"
