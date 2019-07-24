#coding: utf-8

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

perimetro = (a + b + c)

if ((b - c) < a < (b + c)) or ((a - c) < b < (a + c)) or ((a - b) < c < (a + b)):
	print "triangulo valido. %d" % perimetro
	
else:
	print "triangulo invalido."
