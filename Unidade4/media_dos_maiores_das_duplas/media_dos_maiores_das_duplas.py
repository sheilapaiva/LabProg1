#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 4    Questão: Média dos Maiores das Duplas

numero_duplas = int(raw_input())
lista = []
for i in range(numero_duplas):
	dupla = raw_input().split()
	if int(dupla[0]) > int(dupla[1]):
		lista.append(int(dupla[0]))
	elif int(dupla[1]) > int(dupla[0]):
		lista.append(int(dupla[1]))

if len(lista) > 1:
	media = 0.0
	for i in range(len(lista)):
		media += lista[i]
	print "%.2f" % (media / len(lista))
elif len(lista) == 1:
	print "%.2f" % float(lista[0])
else:
	print "Não é possível calcular a média."
