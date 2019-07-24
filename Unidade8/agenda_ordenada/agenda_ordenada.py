#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Agenda Ordenada

def ordenar(lista):
	ta_ordenado = True
	while ta_ordenado  == True:
		ta_ordenado = False
		for i in range(len(lista) -1):
			if lista[i] > lista[i + 1]:
				lista[i], lista[i + 1] = lista[i + 1], lista[i]
				ta_ordenado  = True
				break

	return lista		


agenda = []
while True:
	nome = raw_input()
	if nome == "####": 
		break
	
	agenda.append(nome)
	ordenar(agenda)
	
	for i in agenda:
		if i == nome:
			print "* %s" % nome
		else:
			print i
	print "----"
