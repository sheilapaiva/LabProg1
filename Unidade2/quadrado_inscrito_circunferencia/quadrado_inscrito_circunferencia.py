#coding: utf-8

import math

lado = float(raw_input())

a = (((lado/ 2) ** 2) + ((lado / 2) ** 2))
raio = math.sqrt(a)
circunferencia = (math.pi * (raio * 2))
area = (math.pi * (raio ** 2))

print "Perímetro: %.5f" % circunferencia
print "Área: %.5f" % area
