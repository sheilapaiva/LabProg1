# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Imprime Ranking

numero = int(raw_input())

lista_ranking = []
lista_pontos = []
for i in range(numero):
	nome_time = raw_input()
	pontos_time = int(raw_input())
	lista_pontos.append(str(pontos_time))
	pontos = int(lista_pontos[i-1])
	if i >= 1 and pontos == pontos_time:
		lista_ranking.append("%d. %s (%d)" % (i,nome_time,pontos_time))
	else:
		lista_ranking.append("%d. %s (%d)" % (i+1,nome_time,pontos_time))

for i in range(len(lista_ranking)):
	print lista_ranking[i]
