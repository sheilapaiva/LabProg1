#coding: utf-8

peso_produto_antes_descongelar = float(raw_input())
peso_produto_depois_descongelar = float(raw_input())

diferenca_peso = (peso_produto_antes_descongelar - peso_produto_depois_descongelar)
porcentagem_agua = ((diferenca_peso * 100.0) / peso_produto_antes_descongelar) 

if (porcentagem_agua < 5):
	print "%.1f%% do peso do produto é de água congelada." % porcentagem_agua
	print "Produto qualis A."
	
if (porcentagem_agua >= 5) and (porcentagem_agua < 10):
	print "%.1f%% do peso do produto é de água congelada." % porcentagem_agua
	print "Produto em conformidade."
	
if (porcentagem_agua >= 10):
	print "%.1f%% do peso do produto é de água congelada." % porcentagem_agua
	print "Produto não conforme."
