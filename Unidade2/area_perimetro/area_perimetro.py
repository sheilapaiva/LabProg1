# coding: utf-8
# Área e perímetro de um Círculo

import math

diametro = float(raw_input())

raio = float(diametro / 2)
area = float(math.pi * (raio ** 2))
perimetro = float(2 * math.pi * raio)

print "A: %.5f" % area
print "P: %.5f" % perimetro
