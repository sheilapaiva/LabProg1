#coding: utf-8

veiculo = str(raw_input())

if veiculo == "Automóvel utilitário":
	 print "Valor a pagar: R$ 11.40."
	 
elif veiculo == "Ônibus":
	eixos = int(raw_input())
	valor = (eixos * 11.4)
	print "Valor a pagar: R$ %.2f." % valor
	
elif veiculo == "Caminhão":
	eixos = int(raw_input())
	valor = (eixos * 9.6)
	print "Valor a pagar: R$ %.2f." % valor
	
elif veiculo == "Motocicleta":
	print "Valor a pagar: R$ 5.70."
	
else:
	print "Veículo não cadastrado."
