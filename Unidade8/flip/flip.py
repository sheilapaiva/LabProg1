#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Flip


def flip(lista, i, j):	
	l = range(len(lista))
	ta_ordenado = True
	while ta_ordenado  == True:
		 ta_ordenado = False
		 for k in range(i, j):
			 if l[k] < l[k + 1]:
				 l[k], l[k + 1] = l[k + 1], l[k]
				 lista[k], lista[k + 1] = lista[k + 1], lista[k]
				 ta_ordenado  = True
				 break
				 
	return None
