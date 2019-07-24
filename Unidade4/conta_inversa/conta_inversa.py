# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Conta Inversa

palavra = raw_input()
palavra_inversa = palavra[::-1]

cont = 0
for i in range(len(palavra)):
	letra_palavra = palavra[i]
	letra_palavra_inversa = palavra_inversa[i]
	
	if letra_palavra == letra_palavra_inversa:
		cont += 1

print "A palavra %s contém %d caractere(s) coincidente(s) com a sua inversa." % (palavra, cont)
