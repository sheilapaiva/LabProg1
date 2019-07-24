# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Caixa Preta

numero_medicoes = int(raw_input())

lista = []
cont = 0
parar_if = 0
for i in range(numero_medicoes):
	lista = raw_input().split(" ")
	
	peso = int(lista[0])
	combustivel = int(lista[1])
	altitude = int(lista[2])
		
	if peso >= 0 and parar_if == 0:
		cont += 1
		
	if peso < 0 and parar_if == 0:
		parar_if = 1
		print "dado inconsistente. peso negativo."
		
	if combustivel >= 0 and parar_if == 0:
		cont += 1
		
	if combustivel < 0 and parar_if == 0:
		parar_if = 1
		print "dado inconsistente. combustível negativo."
		
	if altitude >= 0 and parar_if == 0:
		cont += 1
	
	if altitude < 0 and parar_if == 0:
		parar_if = 1
		print "dado inconsistente. altitude negativa."
		
print "%d dados válidos." % cont
