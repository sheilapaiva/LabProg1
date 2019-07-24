#coding: utf-8

salario = float(raw_input())

inss_empregador = (salario * 0.12)

if (salario <= 1317.07):
	inss_empregado = (salario * 0.08)
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % inss_empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % inss_empregado

if (salario >= 1317.08) and (salario <= 2195.12):
	inss_empregado = (salario * 0.09)
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % inss_empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % inss_empregado
	
if (salario > 2195.12):
	inss_empregado = (salario * 0.11)
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % inss_empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % inss_empregado

