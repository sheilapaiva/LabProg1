#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Conta Palavras

def conta_palavras(k, palavras):
	lista_palavras = palavras.split(":")
	cont = 0
	for i in range(len(lista_palavras)):
		if len(lista_palavras[i]) >= k:
			cont += 1
	print lista_palavras
	return cont

assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") == 2

