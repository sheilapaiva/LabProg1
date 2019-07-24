#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Caixa Registradora

def caixa_registradora(lista, meta):
	soma, comissao = 0, 0
	for i in range(len(lista)):
		soma += lista[i]
		if lista[i] < 1000.0:
			comissao += (lista[i] * 5) / 100
		elif lista[i] >= 1000.0 and lista[i] < 5000.0:
			comissao += (lista[i] * 10) / 100
		elif lista[i] >= 5000.0:
			comissao += (lista[i] * 15) / 100

	if (soma - comissao) >= meta:
		situacao = "Lucro"
	else:
		situacao = "Prejuizo"
	
	return [soma, comissao, situacao]

