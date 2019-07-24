#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Aplicação Polinômios

def calcula_polinomio(lista, x):
	resultado = 0
	for i in range(len(lista) -1, 0, -1):
		if i != 0:
			resultado += int(lista[i]) * (int(x[0]) ** (i -1))
		else:
			resultado += int(lista[i])
	print resultado
	return resultado
	

while True:
	sequencia = raw_input().split()
	if sequencia[0] == "fim":
		break
	elif sequencia[0] == "p:":
		polinomio = sequencia
		print "novo polinomio"
	elif len(sequencia) == 1:
		calcula_polinomio(polinomio, sequencia)
