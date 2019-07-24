#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Caixa Alta

def caixa_alta(frase):
	frase_modificada = ""
	frase = " " + frase + " "
	for i in range(1,len(frase) - 1):
		if frase[i - 1] == " " and frase[i + 1] == " ":
			frase_modificada += frase[i].lower()
		elif frase[i - 1] == " " and frase[i + 1] != " ":
			frase_modificada += frase[i].upper()
		elif frase[i - 1] != " " or frase[i + 1] == " ":
			frase_modificada += frase[i]
	return frase_modificada
