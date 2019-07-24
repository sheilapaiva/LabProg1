#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade 4 	Questão: Melhor ataque

quantidade_times = int(raw_input())
total_gols = 0
pontos = 0
lista_times = ""

for i in range(quantidade_times):
	nome_time = str(raw_input())
	quantidade_gols = int(raw_input())
	total_gols += quantidade_gols
		
	if quantidade_gols > pontos:
		pontos = quantidade_gols 
		lista_times = ""
		lista_times += nome_time + "\n"
	elif quantidade_gols == pontos:
		pontos = quantidade_gols 
		lista_times += nome_time + "\n"
		
print "Time(s) com melhor ataque (%d gol(s)):\n%s" % (pontos, lista_times)
media = (total_gols / (quantidade_times * 1.0))
print "Média de gols marcados: %.1f" % media
