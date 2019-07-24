#coding: utf-8

dia_semana = str(raw_input())
quantidade_clientes = int(raw_input())

if dia_semana == "segunda" or dia_semana == "terça" or dia_semana == "quarta" or dia_semana == "quinta" or dia_semana == "sexta":
	if quantidade_clientes >= 40 and quantidade_clientes <= 60:
		print "normal"
	
	else:
		print "atípico"
		
if dia_semana == "sábado" or dia_semana == "domingo":
	if quantidade_clientes >= 40:
		print "normal"
	
	else:
		print "atípico"
