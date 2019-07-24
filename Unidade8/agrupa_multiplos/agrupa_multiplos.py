#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Agrupa Múltiplos

def agrupa_multiplos(seq, k):
	ta_agrupado = True
	while ta_agrupado  == True:
		ta_agrupado = False
		for i in range(len(seq) -1):
			if seq[i] % k != 0 and seq[i + 1] % k == 0:
				seq[i], seq[i + 1] = seq[i + 1], seq[i]
				ta_agrupado = True
				break

	return seq
