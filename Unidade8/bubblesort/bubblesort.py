#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Bubblesort


def bubblesort(dados):	
	ta_ordenado = True
	while ta_ordenado == True:
		ta_ordenado = False
		for i in range(len(dados) -1):
			if dados[i] > dados[i + 1]:
				dados[i], dados[i + 1] = dados[i + 1], dados[i] 
				ta_ordenado = True
	
	return None
