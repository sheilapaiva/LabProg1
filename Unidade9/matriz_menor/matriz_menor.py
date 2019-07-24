#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: Matriz Menor


def matriz_menor(matriz1, matriz2):
	matriz_menor = matriz1
	for i in range(len(matriz1)):
		for j in range(len(matriz1[i])):
			if matriz1[i][j] <= matriz2[i][j]:
				matriz_menor[i][j] = matriz1[i][j]
			else:
				matriz_menor[i][j] = matriz2[i][j]
				
	return matriz_menor
