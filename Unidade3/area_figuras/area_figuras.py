#coding: utf-8

import math

figura = str(raw_input())

if figura == "triângulo":
	base = float(raw_input())
	altura = float(raw_input())
	
	area = float((base * altura) / 2)
	
	print "Área do triângulo: %.2f (cm2)" % area

elif figura == "quadrado":
	lado = float(raw_input())
	
	area = float(lado ** 2)
	
	print "Área do quadrado: %.2f (cm2)" % area
	
elif figura == "círculo":
	raio = float(raw_input())
	
	area = float(math.pi * raio ** 2)
	
	print "Área do círculo: %.2f (cm2)" % area
	
else:
	base = float(raw_input())
	altura = float(raw_input())
	
	area = float(base * altura)
	
	print "Área do retângulo: %.2f (cm2)" % area
	
