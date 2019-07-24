#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 4 	Questão: Coincidentes

palavra1 = raw_input()
palavra2 = raw_input()

print "Letras coincidentes"
cont = 0
for i in range(len(palavra1)):
	if palavra1[i] == palavra2[i]:
		print "'%s' na posição %d" % (palavra1[i], i + 1)
		cont += 1
print "Total de letras coincidentes: %d (%d%%)" % (cont, cont * 100 / (len(palavra1) + len(palavra2)))
