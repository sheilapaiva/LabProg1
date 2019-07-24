#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 4 	Questão: Índices de caracteres

n = int(raw_input())

cont = 0
for i in range(n):
	palavra = raw_input()
	if palavra[0] in "bcdfghjklmnpqrstuvxywz":
		cont += 1
	
print "total de palavras: %d" % n
print "iniciadas por consoantes: %d (%.2f%%)" % (cont, ((cont * 100.) / n))
