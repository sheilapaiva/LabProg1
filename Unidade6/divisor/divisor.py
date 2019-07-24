#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Divisor

def divisor(num, lista):
	indice = -1
	for i in range(len(lista)):
		if lista[i] % num == 0:
			indice = i
			break
	return indice
