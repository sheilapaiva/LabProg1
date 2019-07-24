#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Fundo de Investimento

cont, media, soma = 0, 0, 0
while True:
	investimento = float(raw_input())
	if investimento >= media: 
		cont += 1
		soma += investimento
		media = soma / cont
	else:
		break
print "Saldo total do FIS: R$%.2f." % soma
print "Média das contribuições: R$%.2f." % media
