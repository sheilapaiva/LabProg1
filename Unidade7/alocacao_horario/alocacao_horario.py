#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 7    Questão: Alocação Horário

def get_choque_horario(disciplinas):
	choque_horario, lista_disciplinas = [], []
	lista_disciplinas += disciplinas
	for i in range(len(disciplinas)):
		for j in range(len(lista_disciplinas)):
			if disciplinas[i] != lista_disciplinas[j]:
				disciplina1 = disciplinas[i].split("-")
				disciplina2 = lista_disciplinas[j].split("-")
				if disciplina1[1] == disciplina2[1]:
					choque_horario.append(disciplinas[i])
					break
	
	ta_ordenado = True
	while ta_ordenado  == True:
		 ta_ordenado = False
		 for i in range(len(choque_horario) - 1):
			disciplina = choque_horario[i].split("-")
			a = choque_horario[i + 1].split("-")
			if int(disciplina[1]) > int(a[1]):
				choque_horario[i], choque_horario[i + 1] = choque_horario[i + 1], choque_horario[i]
				ta_ordenado  = True
				break
			
	return choque_horario
	
