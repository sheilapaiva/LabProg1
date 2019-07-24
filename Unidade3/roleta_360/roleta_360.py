#coding: utf-8

num = int(raw_input())

if num > (360 * 5):
	num = num - (360 * 5)
	
if num > (360 * 4):
	num = num - (360 * 4)

if num > (360 * 3):
	num = num - (360 * 3)

if num > (360 * 2):
	num = num - (360 * 2)

if num > 360:
	num = num - 360
	
if 0 < num < 90:
	print "Quadrante 1"

elif 90 < num < 180:
	print "Quadrante 2"

elif 180 < num < 270:
	print "Quadrante 3"
	
elif 270 < num < 360:
	print "Quadrante 4"
	
elif num == 0 or num == 90 or num == 180 or num == 270 or num == 360:
	print "Sobre eixos"
