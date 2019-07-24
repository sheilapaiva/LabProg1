#coding: utf-8
#UFCG - Ciência da Computação
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 4    Questão: Média dos Extremos

n = int(raw_input())

lista_numeros = []
for i in range(n):
	lista_numeros.append(int(raw_input()))
	
maior, menor = 0, lista_numeros[0]
for j in range(len(lista_numeros)):
	if abs(lista_numeros[j]) > maior:
		maior = lista_numeros[j]
	if lista_numeros[j] < menor:
		menor = lista_numeros[j]

media, cont_maior, cont_menor = ((maior + menor) / 2.0), 0, 0
for k in range(len(lista_numeros)):
	if lista_numeros[k] < media:
		cont_menor += 1
	elif lista_numeros[k] > media:
		cont_maior += 1

print "Menor número: %d" % menor
print "Maior número: %d" % maior
print "Média dos extremos: %.2f" % media
print "%d número(s) abaixo da média" % cont_menor
print "%d número(s) acima da média" % cont_maior
