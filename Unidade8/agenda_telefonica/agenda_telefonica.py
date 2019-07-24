#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Agenda Telefônica

def ordenar(lista_nome, lista_telefone):
	ta_ordenado = True
	while ta_ordenado  == True:
		ta_ordenado = False
		for i in range(len(lista_nome) -1):
			if lista_nome[i] > lista_nome[i + 1]:
				lista_nome[i], lista_nome[i + 1] = lista_nome[i + 1], lista_nome[i]
				lista_telefone[i], lista_telefone[i + 1] = lista_telefone[i + 1], lista_telefone[i]
				ta_ordenado  = True
				break

	return lista_nome, lista_telefone	


def inserir(lista_nome, lista_telefone):
	quantidade = int(raw_input())
	for i in range(quantidade):
		lista_nome.append(raw_input())
		lista_telefone.append(raw_input())
		ordenar(lista_nome, lista_telefone)
	
	return lista_nome, lista_telefone
	
	
def buscar(lista_nome, lista_telefone):
	nome = raw_input()
	nome_encontrado = False
	for i in range(len(lista_nome)):
		if nome == lista_nome[i]:
			print "Nome: %s" % lista_nome[i]
			print "Fone: %s" % lista_telefone[i]
			print "----------"
			nome_encontrado = True
	if nome_encontrado == False:
		print "Nome inexistente"
		print "----------"
			
	return lista_nome, lista_telefone
			
			
def imprimir(lista_nome, lista_telefone):
	for i in range(len(lista_nome)):
		print "Nome: %s" % lista_nome[i]
		print "Fone: %s" % lista_telefone[i]
		print "----------"
			
	return lista_nome, lista_telefone
	

agenda_nome, agenda_telefone = [], []
while True:
	operacao = raw_input()
	if operacao == "finalizar": 
		break
	else:
		if operacao == "inserir":
			inserir(agenda_nome, agenda_telefone)
		elif operacao == "buscar":
			buscar(agenda_nome, agenda_telefone)
		elif operacao == "imprimir":
			imprimir(agenda_nome, agenda_telefone)
