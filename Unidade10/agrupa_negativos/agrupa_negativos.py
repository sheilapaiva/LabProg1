#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva  Matrícula: 118210186
#Unidade: 10    Questão: Agrupa Matrículas


def agrupa_negativos(lista):
	negativos, nao_negativos = [], []
	for i in range(len(lista)):
		if lista[i] < 0:
			negativos.append(lista[i])
		else:
			nao_negativos.append(lista[i])
	
	dicionario = {}	
	dicionario["nao-negativos"] = nao_negativos
	dicionario["negativos"] = negativos
	
	return dicionario

