#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 9    Questão: Reduzir matriz


def reduzir_matriz(m):
	for i in range(len(m)):
		if i == 0 or i == len(m) - 1:
			m.pop(i)

	for j in range(len(m) -1, -1, -1):
		m[j].pop(0)
		m[j].pop(len(m[j]) - 1)

	return m
	

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print reduzir_matriz(matriz)
