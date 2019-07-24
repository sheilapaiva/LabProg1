#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Filtra e Altera Lista


def filtra_altera_lista(num, lista):
	for i in range(len(lista) - 1, - 1, - 1):
		if i > 0 and i % num != 0:
			lista.pop(i)

	return lista
