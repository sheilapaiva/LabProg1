#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Char único

def char_unico(string):
	cont_aux, letra_unica = len(string), ""
	for i in range(len(string)):
		cont = 0
		for j in range(len(string)):
			if string[i] == string[j]:
				cont += 1
		print cont
		if cont < cont_aux:
			cont_aux = cont
			letra_unica = string[i] 
			
	return letra_unica
