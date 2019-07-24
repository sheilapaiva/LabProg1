#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Aula de Médias

lista_numeros = []
quantidade_numeros, media, soma = 0, 0.0, 0.0
while True:
	numero = float(raw_input())
	lista_numeros.append(numero)
	soma += numero
	if soma >= 100:
		break
	
print "Quantidade de números lidos: %d" % quantidade_numeros
print "Soma dos números lidos: %.2f" % soma
print "Média = %.2f" % media
print "\nAbaixo da média"

for i in range(len(lista_numeros)):
	if lista_numeros[i] < media:
		print "%.2f (%do)" % (lista_numeros[i], i+1)

print "\nAcima da média"
for i in range(len(lista_numeros)):
	if lista_numeros[i] >= media:
		print "%.2f (%do)" % (lista_numeros[i], i+1)
