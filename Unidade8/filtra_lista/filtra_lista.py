#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Filtra e Altera Lista


def filtra_lista(num, lista):
	nova_lista = []
	for i in range(len(lista)):
		if i % num == 0:
			nova_lista.append(lista[i])

	return nova_lista
