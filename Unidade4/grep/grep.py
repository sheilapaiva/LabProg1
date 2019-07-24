# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Grep

palavra = raw_input()
numero_frases = int(raw_input())

for i in range(numero_frases):
	frase = raw_input()
	lista_palavra_frase = frase.split(" ")
	for j in range(len(lista_palavra_frase)):
		palavra_frase = lista_palavra_frase[j]
		if palavra_frase.find(palavra) != -1:
			print frase
