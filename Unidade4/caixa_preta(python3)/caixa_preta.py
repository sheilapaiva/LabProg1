# coding: utf-8
# Caixa Preta
# Arthur de Amorim Macena
# 118210675
# UFCG - Prog1

quantidade_linhas = int(input())

auxiliar = True
acumulador = 0
for i in range(quantidade_linhas):
	p , c , a = input().split()
	p = int(p)
	c = int(c)
	a = int(a)
	if p < 0 and auxiliar == True:
		auxiliar = False
		print ("dado inconsistente. peso negativo.")
	elif auxiliar == True:
		acumulador += 1
		
	if c < 0 and auxiliar == True:
		auxiliar = False
		print ("dado inconsistente. combustível negativo.")
	elif auxiliar == True:
		acumulador += 1
		
	if a < 0 and auxiliar == True:
		auxiliar = False
		print ("dado inconsistente. altitude negativa.")
	elif auxiliar == True:
		acumulador += 1
		
print ("%d dados válidos." % acumulador)