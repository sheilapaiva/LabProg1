#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 4 	Questão: Ínteiros Positivos Divisíveis

a = int(raw_input())
b = int(raw_input())
k = int(raw_input())

for i in range(1,k + 1):
	if i % a == 0:
		if i % b == 0:
			print i
