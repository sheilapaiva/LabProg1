#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Busca Linear

def busca(seq, valor):
	posicao = -1
	for i in range(len(seq)):
		if seq[i] == valor:
			posicao = i
			break
				
	return posicao
