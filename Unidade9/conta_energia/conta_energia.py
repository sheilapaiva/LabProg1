#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: Conta Energia


def calcula_conta(tabela):
	total_kwh = 0
	for i in range(1, len(tabela)):
		kwh_aparelho = 1
		for j in range(len(tabela[i])):
			if j > 0:
				kwh_aparelho  *= tabela[i][j]
		total_kwh += kwh_aparelho / 1000.0
	
	return "R$ %.2f" % (total_kwh * 0.28)
