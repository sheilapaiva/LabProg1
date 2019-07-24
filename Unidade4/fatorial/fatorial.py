# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Fatorial

numero = int(raw_input())

fatorial = 1
for i in range(2, numero + 1):
	fatorial = fatorial * i
print fatorial
