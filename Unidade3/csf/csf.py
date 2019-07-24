#coding: utf-8

nota_enem = float(raw_input())
creditos = float(raw_input())

if (nota_enem >= 600):
	if (creditos >= 83.2) and (creditos <= 374.4):
		print "Todas as condições satisfeitas."
	
	else:
		print "Condição CRÉDITOS não satisfeita."

if (nota_enem < 600):
	if (creditos >= 83.2) and (creditos <= 374.4):
		print "Condição ENEM não satisfeita."
	
	else:
		print "Nenhuma condição satisfeita."
