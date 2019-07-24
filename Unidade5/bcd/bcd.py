#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: BCD

parte1, lista = "", []
while True:
	numero = raw_input()
	if numero == "fim":
		break
	if len(numero) < 8:
		lista.append("Tente novamente.")
	else:
		parte1 = numero[0] + numero[1] + numero[2] + numero[3]
		parte2 = numero[4] + numero[5] + numero[6] + numero[7]
		if int(parte1, 2) < 10 and int(parte2, 2) < 10:
			lista.append(str(int(parte1, 2)) + str(int(parte2, 2)))
		else:
			lista.append("BCD inválido.")

for i in range(len(lista)):
	print lista[i]
