#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Encontra Menores

def encontra_menores(num, lista):
	menor_numero = -1
	for i in range(len(lista)):
		if lista[i] < num:
			menor_numero = lista[i]
			break
	return menor_numero
