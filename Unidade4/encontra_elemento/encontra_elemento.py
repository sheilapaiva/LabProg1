# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Encontra Elemento

numero = int(raw_input())
sequencia_numeros = list(raw_input().split(" "))

parar_sequencia = 0
numero_sequencia = 0
for i in range(len(sequencia_numeros)):
	numero_sequencia = int(sequencia_numeros[i])
	if numero == numero_sequencia and parar_sequencia == 0:
		print "sim"
		parar_sequencia = 1
if parar_sequencia == 0:
	print "não"
