#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva  Matrícula: 118210186
#Unidade: 10    Questão: Agrupa Matrículas


def meu_in(mapa, procurado):
	encontrou = False
	for elemento in mapa:
		if elemento == procurado:
			mapa[elemento] += 1
			encontrou = True
			break
	if encontrou == False:
		mapa[procurado] = 1


def agrupa_por_periodo(turma):
	periodo_ingresso = []
	for elemento in turma:
		string = ""
		for digito in range(0,3):
			string += elemento[digito]
		periodo_ingresso.append(string)
	
	mapa = {}
	for i in range(len(turma)):
		meu_in(mapa, periodo_ingresso[i])
	
	return mapa
