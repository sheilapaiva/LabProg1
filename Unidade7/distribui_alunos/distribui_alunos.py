#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 7    Questão: Distribui Alunos

def meuin(elemento, lista):
	for i in lista:
		if i == elemento:
			return True
	return False

def distribui_alunos(turma1, turma2, capacidade):
	total, menor = [], 0
	if len(turma1) < len(turma2):
		menor = len(turma1)
	else:
		menor = len(turma2)
		
	for i in range(menor):
		total.append(turma1[i])
		total.append(turma2[i])
		
	if menor == len(turma1) and len(turma1) != len(turma2):
		for j in turma2:
			if meuin(j, total) == False:
				total.append(j)
	elif menor == len(turma2) and len(turma1) != len(turma2):
		for j in turma1:
			if meuin(j, total) == False:
				total.append(j)
				
	distribuido = [[], []]
	for e in total:
		if len(distribuido[0]) < capacidade:
			distribuido[0].append(e)
		else:
			distribuido[1].append(e)
		
	return distribuido
