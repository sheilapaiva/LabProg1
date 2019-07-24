#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Cria Login

def cria_login(nome):
	lista_nomes = nome.split()
	nome1 = lista_nomes[0].lower()
	for i in range(1, len(lista_nomes)):
		if lista_nomes[i] != "da" and lista_nomes[i] != "de" and lista_nomes[i] != "do":
			nome1 += lista_nomes[i][0].lower()
	
	print "%s: %s" % (nome, nome1)


while True:
	nome_completo = raw_input()
	if nome_completo == "fim":
		break
	else:
		cria_login(nome_completo)
