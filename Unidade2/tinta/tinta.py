# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 1 	Questão: Pintor

altura = float(raw_input())
largura = float(raw_input())

area_parede = (altura * largura)
galao_metro_quadrado = (3.6 / 50)
litros_tinta = (area_parede * galao_metro_quadrado)

print "%.2f l" % litros_tinta
