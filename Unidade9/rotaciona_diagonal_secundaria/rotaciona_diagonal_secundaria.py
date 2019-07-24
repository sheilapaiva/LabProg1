#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva  Matrícula: 118210186
#Unidade: 9    Questão: Rotaciona Diagonal Secundária


def rotaciona_ds(matriz, direcao):
	lin = 0
	col = len(matriz) - 1
	for loop in range(len(matriz) - 1):
		if direcao == "cima":
			matriz[lin][col], matriz[lin + 1][col - 1] =  matriz[lin + 1][col - 1], matriz[lin][col]
		elif direcao == "baixo":
			matriz[col][lin], matriz[col - 1][lin + 1] =  matriz[col - 1][lin + 1], matriz[col][lin]
		lin += 1
		col -= 1
		
	return None
