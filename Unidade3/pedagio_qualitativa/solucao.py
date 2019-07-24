# coding: utf-8

v = raw_input()

if v == "Automóvel utilitário":
	p = 11.40
	print "Valor a pagar: R$ %.2f." % p
elif v == "Ônibus":
	eixos = int(raw_input())
	p = eixos * 11.40
	print "Valor a pagar: R$ %.2f." % p
elif v == "Caminhão":
	eixos = int(raw_input())
	p = eixos * 9.60
	print "Valor a pagar: R$ %.2f." % p
elif v == "Motocicleta":
	p = 5.70
	print "Valor a pagar: R$ %.2f." % p
else:
	print "Veículo não cadastrado."
