#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Imprime Sequencias

numero_alvo = int(raw_input())
lista_maiores, cont = [], 0
while True:
	sequencia = raw_input()
	if sequencia == "fim":
		break
	else:
		cont += 1
		lista_sequencia = sequencia.split()
		conta_maiores = 0
		for i in range(len(lista_sequencia)):
			if int(lista_sequencia[i]) > numero_alvo:
				conta_maiores += 1 
		if conta_maiores > (len(lista_sequencia) / 2):
			lista_maiores.append("sequencia %d: %s" % (cont, sequencia))
for i in range(len(lista_maiores)):
	print lista_maiores[i]

