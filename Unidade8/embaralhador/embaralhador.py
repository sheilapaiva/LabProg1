#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Embaralhador


def embaralhador_ge(sequencia_cartas):
	cont = 1
	while cont < len(sequencia_cartas):
		cont += 1
		for i in range(len(sequencia_cartas) - 1):
			sequencia_cartas[i], sequencia_cartas[i + 1] = sequencia_cartas[i + 1], sequencia_cartas[i]
			
	sequencia = ""
	for i in range(len(sequencia_cartas)):
		if i < len(sequencia_cartas) - 1:
			sequencia += sequencia_cartas[i] + " "
		else:
			sequencia += sequencia_cartas[i]
	print sequencia
	return sequencia_cartas
	
	
def embaralhador_gd(sequencia_cartas):
	for i in range(len(sequencia_cartas) - 1):
		sequencia_cartas[i], sequencia_cartas[i + 1] = sequencia_cartas[i + 1], sequencia_cartas[i]
			
	sequencia = ""
	for i in range(len(sequencia_cartas)):
		if i < len(sequencia_cartas) - 1:
			sequencia += sequencia_cartas[i] + " "
		else:
			sequencia += sequencia_cartas[i]
	print sequencia
	return sequencia_cartas


def embaralhador_i(sequencia_cartas):
	for i in range(0, len(sequencia_cartas) - 1, 2):
		sequencia_cartas[i], sequencia_cartas[i + 1] = sequencia_cartas[i + 1], sequencia_cartas[i]
			
	sequencia = ""
	for i in range(len(sequencia_cartas)):
		if i < len(sequencia_cartas) - 1:
			sequencia += sequencia_cartas[i] + " "
		else:
			sequencia += sequencia_cartas[i]
	print sequencia
	return sequencia_cartas


sequencia_cartas = raw_input().split()

while True:
	codigo_operacao = raw_input()
	
	if codigo_operacao == "fim":
		break
	
	else:
		if codigo_operacao == "GE":
			embaralhador_ge(sequencia_cartas)
		elif codigo_operacao == "GD":
			embaralhador_gd(sequencia_cartas)
		elif codigo_operacao == "I":
			embaralhador_i(sequencia_cartas)
