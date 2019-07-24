# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Classifica Letra

palavra = raw_input()

for i in range(len(palavra)):
	letra = palavra[i]
	if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
		print "<%s> sim" % letra
	else:
		print "<%s> nao" % letra
