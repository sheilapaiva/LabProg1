# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Converte Senha

senha = raw_input()
lista_senha = list(senha)

cont = 0
for i in range(len(senha)):
	if i > 0:
		if lista_senha[i] == "a" or lista_senha[i] == "A":
			lista_senha[i] = "4"
			cont += 1
		elif lista_senha[i] == "e" or lista_senha[i] == "E":
			lista_senha[i] = "3"
			cont += 1
		elif lista_senha[i] == "i" or lista_senha[i] == "I":
			lista_senha[i] = "1"
			cont += 1
		elif lista_senha[i] == "o" or lista_senha[i] == "O":
			lista_senha[i] = "0"
			cont += 1

nova_senha = ""
for i in range(len(senha)):
	nova_senha += lista_senha[i] 

print "%s (%d troca(s))" % (nova_senha, cont)
