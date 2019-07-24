#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Agrupa Próximos

def agrupa_proximos(lista, valor, criterio):
	l = []
	for i in range(len(lista)):
		if abs(lista[i] - valor) < criterio:
			l.append(lista[i])
	return l
