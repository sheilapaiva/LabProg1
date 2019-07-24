#coding: utf-8

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
nota4 = float(raw_input())

media = ((nota1 + nota2 + nota3 + nota4) / 4)

if media >= 9:
	print "Conceito A."
elif media >= 7.5 and media < 9:
	print "Conceito B."
elif media >= 6 and media < 7.5:
	print "Conceito C."
elif media >= 4 and media < 6:
	print "Conceito D."
else:
	print "Conceito E."
