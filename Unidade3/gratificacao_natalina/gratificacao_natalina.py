#coding: utf-8

codigo = int(raw_input())

if codigo == 1:
	print "Deverá receber em dezembro R$ 25000.00."
	
if codigo == 2:
	print "Deverá receber em dezembro R$ 15000.00."
	
if codigo == 3:
	faltas = int(raw_input())
	if faltas >= 1:
		gratificacao = ((235 - faltas) * 2.)
		salario = (8000 + gratificacao)
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
	else:
		gratificacao = 500.
		salario = (8000 + gratificacao)
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario

if codigo == 4:
	faltas = int(raw_input())
	if faltas >= 1:
		gratificacao = ((235 - faltas) * 1.)
		salario = (5000 + gratificacao)
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
	else:
		gratificacao = 300.
		salario = (5000 + gratificacao)
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
	
if codigo == 5:
	faltas = int(raw_input())
	if faltas >= 1:
		gratificacao = ((235 - faltas) * 0.7)
		salario = (2800 + gratificacao)
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
	else:
		gratificacao = 200.
		salario = (2800 + gratificacao)
		print "Valor da gratificação R$ %.2f." % gratificacao
		print "Deverá receber em dezembro R$ %.2f." % salario
