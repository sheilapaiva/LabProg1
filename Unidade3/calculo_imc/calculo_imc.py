#coding: utf-8

peso = float(raw_input())
altura = float(raw_input())

imc = float(peso / altura ** 2)

if imc < 16:
	print "IMC: %.1f - Magreza grave" % imc
if 16 <= imc < 17:	
	print "IMC: %.1f - Magreza moderada" % imc
if 17 <= imc < 18.5:
	print "IMC: %.1f - Magreza leve" % imc
if 18.5 <= imc < 25:
	print "IMC: %.1f - Saudável" % imc
if 25 <= imc < 30:	
	print "IMC: %.1f - Sobrepeso" % imc
if 30 <= imc < 35:	
	print "IMC: %.1f - Obesidade Grau I" % imc
if 35 <= imc < 40:	
	print "IMC: %.1f - Obesidade Grau II (severa)" % imc
if imc >= 40:
	print "IMC: %.1f - Obesidade Grau III (mórbida)" % imc
