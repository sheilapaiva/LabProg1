#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Calculadora

while True:
	lista = raw_input().split(" ")
	
	if len(lista) < 3:
		break
		
	operacao = int(lista[0])
	operando1 = int(lista[1])
	operando2 = int(lista[2])
	
	if operacao == 1:
		print operando1 + operando2
	
	elif operacao == 2:
		print operando1 - operando2
	
	elif operacao == 3:
		print operando1 * operando2
	
	elif operacao == 4:
		if operando2 == 0:
			print "Erro: Divisão por 0"
			break
		else:
			print operando1 / operando2
	
	elif operacao == 5:
		break
