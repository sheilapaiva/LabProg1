#coding: utf-8

altura = int(raw_input())
numero_o = 1
numero_espacos = 0 

for arvore in range(altura):
	print " " * (numero_espacos + (altura -1)) + numero_o * "o"
	numero_o +=2
	numero_espacos -= 1

print (altura - 1) * " " + "o"
