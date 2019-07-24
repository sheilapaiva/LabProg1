#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: É Quadrado Mágico?


def ha_repetidos(m):
	for i in range(len(m)):
		for j in range(len(m[i])):
			for k in range(len(m)):
				for l in range(len(m[k])):
					if i != k and j != l and m[i][j] == m[k][l]:
						return True
	return False


def numero_linhas_colunas(m):
	cont_colunas = 0
	for j in range(len(m[0])):
		cont_colunas += 1
	if cont_colunas == len(m):
		return True
	return False


def sao_iguais(lista):
	eh_igual = 0
	for k in range(len(lista)):
		for l in range(len(lista)):
			if lista[k] == lista[l] and k != l:
				eh_igual += 1
				break
	if eh_igual == (len(lista)):
		return True
	else:	
		return False


def somar_linhas(m):
	somas = []
	for i in range(len(m)):
		soma = 0
		for j in range(len(m[i])):
			soma += m[i][j]
		somas.append(soma)
		
	if sao_iguais(somas) == True:
		return somas[0]
	elif sao_iguais(somas) == False:
		return 0
	
	
def soma_colunas(m):
	somas = []
	for j in range(len(m[0])):
		soma = 0
		for i in range(len(m)):
			soma += m[i][j]
		somas.append(soma)
	
	if sao_iguais(somas) == True:
		return somas[0]
	elif sao_iguais(somas) == False:
		return 0


def soma_diagonal_principal(m):
	somas =  0
	for i in range(len(m)):
		soma = 0
		for j in range(len(m[i])):
			if i == j:
				soma += m[i][j]
		somas += soma
	return somas
	
	
def soma_diagonal_secundaria(m):
	somas = 0
	for i in range(len(m)):
		soma = 0
		for j in range(len(m[i])):
			if j == (len(m) - 1 - i):
				soma += m[i][j]
		somas += soma
	return somas


def eh_quadrado_magico(matriz):
	if numero_linhas_colunas(matriz) == True:
		if ha_repetidos(matriz) == False:
			todas_somas = []
			todas_somas.append(somar_linhas(matriz))
			todas_somas.append(soma_colunas(matriz))
			todas_somas.append(soma_diagonal_principal(matriz))
			todas_somas.append(soma_diagonal_secundaria(matriz))
			print todas_somas
			if sao_iguais(todas_somas) == True:
				return True
			else:
				return False
	return False
