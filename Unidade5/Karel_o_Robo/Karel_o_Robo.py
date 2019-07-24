#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Karel o Robô
x, y = 0, 0
while True:
	coordenada = raw_input().split()
	direcao = coordenada[0]
	unidade_movimento = int(coordenada[1])
	if unidade_movimento == 0:
		print "Fim de jogo"
		break
	else:
		if direcao == "E":
			x -= unidade_movimento
		elif direcao == "D":
			x += unidade_movimento
		elif direcao == "B":
			y -= unidade_movimento
		elif direcao == "C":
			y += unidade_movimento
	if abs(x) > 0 and abs(y) == abs(x) * 2:
		print "Parabéns, conquista do portal (%d, %d)" % (x, y)
		break
