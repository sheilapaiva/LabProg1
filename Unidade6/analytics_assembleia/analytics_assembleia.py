#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Analytics Assembleia

def conta_votos(votacoes,id_votacao):
	lista, cont_sim, cont_nao = [], 0, 0
	for i in range(len(votacoes)):
		lista = votacoes[i].split(",")
		if int(lista[2]) == id_votacao:
			if lista[1] == "sim":
				cont_sim += 1
			elif lista[1] == "nao":
				cont_nao += 1
	return [cont_sim, cont_nao]
