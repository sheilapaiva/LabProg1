#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva  Matrícula: 118210186
#Unidade: 10    Questão: Colegas de Sala


def colegas_de_sala(dicionario, nome_prof):
	colegas_de_sala_professor = []
	for num in dicionario:
		if dicionario[num] == dicionario[nome_prof] and num != nome_prof:
			colegas_de_sala_professor.append(num)

	return colegas_de_sala_professor
