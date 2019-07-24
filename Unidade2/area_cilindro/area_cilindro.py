#coding: utf-8

import math

print "Cálculo da Superfície de um Cilindro"
print "---"

diametro = float(raw_input("Medida do diâmetro? "))
altura = float(raw_input("Medida da altura? "))
print "---"

raio = (diametro / 2)
area_lateral = (2 * math.pi * raio * altura)
area_base = (math.pi * (raio ** 2))
area_total = (area_lateral + (2 * area_base))

print "Área calculada: %.2f" % area_total
