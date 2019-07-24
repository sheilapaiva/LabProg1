#coding: utf-8

import math

raio = float(raw_input())

area_circunferencia = (math.pi * (raio ** 2))
lado_quadrado = (raio * math.sqrt(2))
area_quadrado = (lado_quadrado ** 2)
diferenca = (area_circunferencia - area_quadrado)

print "Área não comum: %.5f" % diferenca
