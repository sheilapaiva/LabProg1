# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Calcula DV

numero_conta = raw_input()
lista = list(numero_conta)

somar_numero_posicoes_pares = 0
for i in range(len(lista)):
	lista[i] = int(lista[i])
	if i % 2 == 0:
		somar_numero_posicoes_pares += lista[i]

somar_numero_posicoes_impares = 0
for i in range(len(lista)):
	lista[i] = int(lista[i])
	if i % 2 != 0:
		somar_numero_posicoes_impares += lista[i]

digito_verificador = ((somar_numero_posicoes_pares * somar_numero_posicoes_impares) % 11)
if digito_verificador == 10:
	print "%s-X" % numero_conta
else:
	print "%s-%d" % (numero_conta, digito_verificador)
