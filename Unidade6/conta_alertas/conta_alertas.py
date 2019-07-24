#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Conta Alertas

def conta_alertas_acude(medicoes):
	cont = 0
	for i in range(len(medicoes)):
		if medicoes[i] < 17 and abs(medicoes[i] - medicoes[i - 1]) < 10:
			cont += 1
	return cont
