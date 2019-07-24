#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: Busca por Coluna


def busca_todos_por_coluna_em_matriz(m, e):
	lista = []
	for j in range(len(m[0])):
		for i in range(len(m)):
			if  m[i][j] == e:
				lista.append((i,j))
	return lista
