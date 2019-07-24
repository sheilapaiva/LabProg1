#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Cálculo de Seguro

def calcula_seguro(valor_carro, lista):
	pontuacao = 0
	if lista[0] <= 21:
		pontuacao += 20
	elif lista[0] >= 22 and lista[0] <= 30:
		pontuacao += 15
	elif lista[0] >= 31 and lista[0] <= 40:
		pontuacao += 12
	elif lista[0] >= 41 and lista[0] <= 60:
		pontuacao += 10
	elif lista[0] > 60:
		pontuacao += 20
		
	if lista[1] == True:
		pontuacao += 10
	elif lista[1] == False:
		pontuacao += 20
		
	if lista[2] == True:
		pontuacao += 20
	elif lista[2] == False:
		pontuacao += 10
		
	if lista[3] == True:
		pontuacao += 20
	elif lista[3] == False:
		pontuacao += 10
		
	if lista[4] == True:
		pontuacao += 20
	elif lista[4] == False:
		pontuacao += 10
		
	if lista[5] == True:
		pontuacao += 10
	elif lista[5] == False:
		pontuacao += 20
		
	if lista[6] == "Lazer":
		pontuacao += 20
	elif lista[6] == "Misto":
		pontuacao += 20
	elif lista[6] == "Trabalho":
		pontuacao += 10
		
	if pontuacao <= 80:
		risco = "Risco Baixo"
		valor_seguro = valor_carro * 0.1
	elif pontuacao > 80 and pontuacao <= 100:
		risco = "Risco Medio"
		valor_seguro = valor_carro * 0.2
	elif pontuacao > 100:
		risco = "Risco Alto"
		valor_seguro = valor_carro * 0.3
	 
	return [pontuacao, risco, valor_seguro]
