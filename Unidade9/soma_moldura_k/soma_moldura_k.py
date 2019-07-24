#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: Soma Moldura k


def soma_moldura(m, k):
	soma = 0
	for i in range(k, len(m) - k):
		for j in range(k, len(m[i]) - k):
			if i == k:
				soma += m[i][j]
			elif i == len(m) - 1 - k:
				soma += m[i][j]
			elif j == k:
				soma += m[i][j]
			elif j == len(m) - 1 - k:
				soma += m[i][j]	
	return soma
