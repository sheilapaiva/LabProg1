#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Analytics Votação

def conta_votos(votacoes,id_votacao):
	lista, cont_sim, cont_nao = [], 0, 0
	for i in range(len(votacoes)):
		lista = votacoes[i].split(",")
		if int(lista[1]) == id_votacao:
			if lista[4] == "sim":
				cont_sim += 1
			elif lista[4] == "nao":
				cont_nao += 1
	return [cont_sim, cont_nao]
