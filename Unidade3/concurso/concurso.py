#coding: utf-8

nota1_candidato1 = float(raw_input())
nota2_candidato1 = float(raw_input())
nota3_candidato1 = float(raw_input())
idade_candidato1 = int(raw_input())
nota1_candidato2 = float(raw_input())
nota2_candidato2 = float(raw_input())
nota3_candidato2 = float(raw_input())
idade_candidato2 = int(raw_input())

media_cadidato1 = (((nota1_candidato1 * 0.3) + (nota2_candidato1 * 0.4) + (nota3_candidato1 * 0.3)) / 1)
media_cadidato2 = (((nota1_candidato2 * 0.3) + (nota2_candidato2 * 0.4) + (nota3_candidato2 *  0.3)) / 1)

if (media_cadidato1 > media_cadidato2):
	print "O primeiro candidato foi aprovado com média %.1f." % media_cadidato1

if (media_cadidato1 < media_cadidato2):
	print "O segundo candidato foi aprovado com média %.1f." % media_cadidato2
	
if (media_cadidato1 == media_cadidato2):
	if (idade_candidato1 > idade_candidato2):
		print "O primeiro candidato foi aprovado com média %.1f." % media_cadidato1
		
	if (idade_candidato1 < idade_candidato2):
		print "O segundo candidato foi aprovado com média %.1f." % media_cadidato2
		
	if (idade_candidato1 == idade_candidato2):
		print "Empate."
