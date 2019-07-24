#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: Busca em Matriz


def busca_matriz(m, e):
	for i in range(len(m)):
		for j in range(len(m[i])):
			if  m[i][j] == e:
				return (i,j)
	return None	
