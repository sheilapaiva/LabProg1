#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Cria Senha


def criaSenhaFraca(palavra):
	senha_nova = "((" + palavra + "))"
	print senha_nova
	

def criaSenhaForte(palavra):
	senha_nova = "(("
	for i in palavra:
		if i == "o" or i == "O":
			senha_nova += "0"
		elif i == "i" or i == "I" or i == "L" or i == "l":
			senha_nova += "1"
		elif i == "e" or i == "E":
			senha_nova += "3"
		elif i == "a" or i == "A":
			senha_nova += "4"
		elif i == "b" or i == "B":
			senha_nova += "6"
		elif i == "t" or i == "T":
			senha_nova += "7"
		else:
			senha_nova += i
		
	senha_nova += "))"
	print senha_nova


while True:
	palavras = raw_input()
	if palavras == "***":
		break
	else:
		senha, nivel_seguranca = palavras.split()
		if nivel_seguranca == "fraco":
			criaSenhaFraca(senha)
		elif nivel_seguranca == "forte":
			criaSenhaForte(senha)
