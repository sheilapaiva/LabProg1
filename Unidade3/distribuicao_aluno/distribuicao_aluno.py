#coding: utf-8

unidade = int(raw_input())
deseja_pular = str(raw_input())
quantidade_questoes_unidade = int(raw_input())

if deseja_pular == "nao" or deseja_pular == "não":
	if unidade >= 1 and unidade <= 4:
		print "O aluno deve assistir aula com o prof João."

	elif unidade >= 5 and unidade <= 8:
		print "O aluno deve assistir aula com o prof Dalton."

	else:
		print "O aluno deve assistir aula com o prof Jorge."
	
if deseja_pular == "sim":
	if quantidade_questoes_unidade >= 1:
		if unidade >= 1 and unidade < 4:
			print "O aluno deve assistir aula com o prof João."

		elif unidade >= 4 and unidade < 8:
			print "O aluno deve assistir aula com o prof Dalton."

		else:
			print "O aluno deve assistir aula com o prof Jorge."
	
	if quantidade_questoes_unidade == 0:
		if unidade >= 1 and unidade <= 4:
			print "O aluno deve assistir aula com o prof João."

		elif unidade >= 5 and unidade <= 8:
			print "O aluno deve assistir aula com o prof Dalton."

		else:
			print "O aluno deve assistir aula com o prof Jorge."
