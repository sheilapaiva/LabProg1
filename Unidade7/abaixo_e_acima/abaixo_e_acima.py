#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 7 	Questão: Abaixo e Acima

def  organiza_por_media(lista):
	if len(lista) > 0:
		soma = 0.
		for i in range(len(lista)):
			soma += lista[i] 
		media = soma / len(lista)

	aux = []
	for j in range(len(lista) - 1, -1, -1):
		if lista[j] > media:
			aux.append(lista[j])
			lista.pop(j)

	for k in range(len(aux) - 1, -1, -1):
		lista.append(aux[k])
	
	return lista

p1 = [1, 2, 4, 1, 3, 4, 56, 7, 7, 4, 3, 67]
print organiza_por_media(p1) 
