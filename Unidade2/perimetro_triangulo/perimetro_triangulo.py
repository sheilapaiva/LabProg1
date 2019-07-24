#coding: utf-8

import math

x1 = int(raw_input())
y1 = int(raw_input())
x2 = int(raw_input())
y2 = int(raw_input())
x3 = int(raw_input())
y3 = int(raw_input())

perimetro1 = float(math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)))
perimetro2 = float(math.sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2)))
perimetro3 = float(math.sqrt(((x2 - x3) ** 2) + ((y2 - y3) ** 2)))
area = (perimetro1 + perimetro2 + perimetro3)

print "O perímetro é de %.2f" % area
