#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Critérios Diferentes

def ordena(lista1,lista2):
	lista_nova = []
	
	for elemento_l1 in lista1:
		lista_nova.append(elemento_l1)
		
	for elemento_l2 in lista2:
		lista_nova.append(elemento_l2)
		
	ta_ordenado = True
	while ta_ordenado  == True:
		 ta_ordenado = False
		 for i in range(len(lista_nova) -1):
			 if lista_nova[i] > lista_nova[i + 1]:
				 lista_nova[i], lista_nova[i + 1] = lista_nova[i + 1], lista_nova[i]
				 ta_ordenado  = True
				 break

	return lista_nova
