#coding: utf-8

salario_base = float(raw_input())
quantidade_dias_trabalhados = int(raw_input())
custo_diario_transporte = float(raw_input())

vale_transporte = (custo_diario_transporte * quantidade_dias_trabalhados)
fgts_inss = (salario_base * 0.2)

if salario_base <= 1317.07 and vale_transporte <= (salario_base * 0.06):
	print "O salário base é R$ %.2f" % salario_base
	print "O custo mensal para o empregador é de R$ %.2f" % (salario_base + fgts_inss)
	print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % (salario_base * 0.92)
	
elif 1317.08 <= salario_base and vale_transporte <= (salario_base * 0.06):
	print "O salário base é R$ %.2f" % salario_base
	print "O custo mensal para o empregador é de R$ %.2f" % (salario_base + fgts_inss)
	print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % (salario_base * 0.91)

elif salario_base >= 2195.13 and vale_transporte <= (salario_base * 0.06):
	print "O salário base é R$ %.2f" % salario_base
	print "O custo mensal para o empregador é de R$ %.2f" % (salario_base + fgts_inss)
	print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % (salario_base * 0.89)
	
elif salario_base <= 1317.07 and vale_transporte >= (salario_base * 0.06):
	print "O salário base é R$ %.2f" % salario_base
	print "O custo mensal para o empregador é de R$ %.2f" % (salario_base + fgts_inss + vale_transporte - (salario_base * 0.06))
	print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % (salario_base - (salario_base * 0.08) - (salario_base * 0.06))
	
elif 1317.08 <= salario_base <= 2195.12 and vale_transporte >= (salario_base * 0.06):
	print "O salário base é R$ %.2f" % salario_base
	print "O custo mensal para o empregador é de R$ %.2f" % (salario_base + fgts_inss + vale_transporte - (salario_base * 0.06))
	print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % (salario_base - (salario_base * 0.09) - (salario_base * 0.06))
	
else:
	print "O salário base é R$ %.2f" % salario_base
	print "O custo mensal para o empregador é de R$ %.2f" % (salario_base + fgts_inss + vale_transporte - (salario_base * 0.06))
	print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % (salario_base - (salario_base * 0.11) - (salario_base * 0.06))
