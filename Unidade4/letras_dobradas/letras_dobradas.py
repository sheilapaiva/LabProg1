#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 4 	Questão: Letras Dobradas

n = int(raw_input())

letras_dobradas, sem_letras_dobradas = [], []
cont_dobradas, cont_sem_dobradas = 0, 0
for i in range(n):
	palavra = raw_input()
	palavra_auxiliar = ""
	for j in range(len(palavra)):
		if palavra[j] == palavra[j - 1]:
			palavra_auxiliar = palavra
	if palavra_auxiliar != "":
		letras_dobradas.append(palavra)
		cont_dobradas += 1
	else:
		sem_letras_dobradas.append(palavra)
		cont_sem_dobradas += 1

print "%d palavra(s) com letras dobradas:" % (cont_dobradas)
for i in range(len(letras_dobradas)):
	print letras_dobradas[i]
print "---"
print "%d palavra(s) sem letras dobradas:" % (cont_sem_dobradas)
for i in range(len(sem_letras_dobradas)):
	print sem_letras_dobradas[i]

