#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 7    Questão: Desloca Elemento

def desloca(lista, origem, destino):
	deslocar = True
	elemento_origem = lista[origem]
	while deslocar == True:
		deslocar = False
		for i in range(len(lista) -1):
			if lista[i] == elemento_origem and lista[destino] != elemento_origem:
				lista[i], lista[i + 1] = lista[i + 1], lista[i]
				deslocar = True
				break
	
	return None
