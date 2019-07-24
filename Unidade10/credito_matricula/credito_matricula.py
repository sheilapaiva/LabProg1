#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva  Matrícula: 118210186
#Unidade: 10    Questão: Crédito Matrícula


def num_creditos(bd_ufcg, matricula):
	contar_creditos = 0
	for ua in bd_ufcg:
		for disc in bd_ufcg[ua]:
			for mat in range(len(bd_ufcg[ua][disc])):
				if bd_ufcg[ua][disc][mat] == matricula:
					contar_creditos += disc[1]
	
	return contar_creditos
