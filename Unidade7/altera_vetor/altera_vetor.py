#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 7    Questão: Altera Vetor

def altera_vetor_por_escalar(vetor, escalar):
	for i in range(len(vetor)):
		vetor[i] = (vetor[i] * escalar)

	return None
