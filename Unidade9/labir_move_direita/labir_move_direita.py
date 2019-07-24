#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: Labir Move Direita


def move_direita(labirinto):
	pode_mover = False
	for i in range(len(labirinto)):
		for j in range(len(labirinto[i])):
			if labirinto[i][j] == "*":
				if j == len(labirinto[i]) - 1:
					return (i, j)
				else:
					pode_mover = True
			elif pode_mover == True:
				if labirinto[i][j] == " ":
					labirinto[i][j], labirinto[i][j - 1] = labirinto[i][j - 1], labirinto[i][j]
					return (i, j)
				elif labirinto[i][j] == "P":
					return (i, j - 1)
