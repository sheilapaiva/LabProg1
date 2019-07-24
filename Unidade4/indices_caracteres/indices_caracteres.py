#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 4 	Questão: Índices de caracteres

palavra1 = raw_input()
palavra2 = raw_input()

for i in range(len(palavra2)):
	indices = ""
	for j in range(len(palavra1)):
		if palavra2[i] == palavra1[j] and len(indices) > 0:
			indices += " " + str(j)
		elif palavra2[i] == palavra1[j] and indices == "":
			indices += str(j)
	if indices == "":
		print -1
	else:
		print indices
