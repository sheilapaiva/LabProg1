#coding: utf-8

opcao = int(raw_input())

if opcao == 1:
	tamanho_tanque = float(raw_input())
	valor = (tamanho_tanque * 80.)
	print "R$ %d,00" % valor
	if valor >= 200:
		print "Brinde!"

if opcao == 2:
	tamanho_tanque = float(raw_input())
	valor = (tamanho_tanque * 50.)
	print "R$ %d,00" % valor
	if valor >= 200:
		print "Brinde!"
	
if opcao == 3:
	print "R$ 50,00"
