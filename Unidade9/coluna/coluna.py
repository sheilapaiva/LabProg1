#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: Coluna


def coluna(matriz, c):
	valores_coluna = []
	for j in range(len(matriz[0])):
		for i in range(len(matriz)):
			if  j == c:
				valores_coluna.append(matriz[i][j])
	return valores_coluna
