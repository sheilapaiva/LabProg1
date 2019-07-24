#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 7    Questão: Ajeita Lista

def separa_par_impar(lista):
	ta_separado = True
	while ta_separado == True:
		 ta_separado = False
		 for i in range(len(lista) -1):
			 if lista[i] % 2 != 0 and lista[i + 1] % 2 == 0:
				 lista[i], lista[i + 1] = lista[i + 1], lista[i]
				 ta_separado = True
				 break
	return lista

def ordenar_par_decrescente(lista):
	ta_ordenado = True
	while ta_ordenado  == True:
		 ta_ordenado = False
		 for i in range(len(lista) -1):
			 if lista[i] % 2 == 0 and lista[i + 1] % 2 == 0:
				 if lista[i] < lista[i + 1]:
					 lista[i], lista[i + 1] = lista[i + 1], lista[i]
					 ta_ordenado  = True
					 break
					 
def ordenar_impar_crescente(lista):
	ta_ordenado = True
	while ta_ordenado  == True:
		 ta_ordenado = False
		 for i in range(len(lista) -1):
			 if lista[i] % 2 != 0 and lista[i + 1] % 2 != 0:
				 if lista[i] > lista[i + 1]:
					 lista[i], lista[i + 1] = lista[i + 1], lista[i]
					 ta_ordenado  = True
					 break

def ajeita_lista(lista):
	separa_par_impar(lista)
	ordenar_par_decrescente(lista)
	ordenar_impar_crescente(lista)
	
	return None
