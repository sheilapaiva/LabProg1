#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 3    Questão: Seleção Projeto

cre = float(raw_input())
experiencia_meses = int(raw_input())
nota_entrevista = int(raw_input())

if cre < 7 and experiencia_meses < 6:
	print "Candidato eliminado. CRE e experiência abaixo do limite."
elif cre < 7 and experiencia_meses >= 6:
	print "Candidato eliminado. CRE abaixo do limite."
elif cre >= 7 and experiencia_meses < 6:
	print "Candidato eliminado. Experiência abaixo do limite."
elif cre >= 7 and experiencia_meses >= 6:
	if nota_entrevista <= 3:
		print "Candidato classificado."
	elif nota_entrevista > 3:
		print "Candidato aprovado."
