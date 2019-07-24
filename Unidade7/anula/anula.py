#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 7    Questão: Anula

def anula(lista):
	anular = True
	while anular == True:
		anular = False
		for i in range(len(lista) -1):
			if (lista[i] + lista[i + 1]) == 0:
				lista.pop(i + 1)
				lista.pop(i)
				anular = True
				break
			
	return None
