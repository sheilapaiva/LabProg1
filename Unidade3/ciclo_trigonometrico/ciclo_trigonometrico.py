#coding: utf-8

grau = int(raw_input())

if (0 < grau < 90) or (0 < (grau % 360) < 90):
	print "Quadrante 1"

elif (90 < grau < 180) or (90 < (grau % 360) < 180):
	print "Quadrante 2"

elif (180 < grau < 270) or (180 < (grau % 360) < 270):
	print "Quadrante 3"

elif (270 < grau < 360) or (270 < (grau % 360) < 360):
	print "Quadrante 4"

else:
	print "Sobre eixos"
