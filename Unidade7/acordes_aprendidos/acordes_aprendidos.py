#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Analytics Votação

def meuin(elemento, lista):
	for i in lista:
		if i == elemento:
			return True
	return False

def acordes(musica_1, musica_2):
	lista_acordes = []
	for i in musica_1:
		lista_acordes.append(i)
		
	for j in musica_2:
		if meuin(j,musica_1) == False:
			lista_acordes.append(j)
	
	return lista_acordes
