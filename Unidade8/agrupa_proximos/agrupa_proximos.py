#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Agrupa Próximos

def agrupa_proximos(lista, valor, criterio):
	l = []
	for i in range(len(lista)):
		if abs(lista[i] - valor) < criterio:
			l.append(lista[i])
	return l
