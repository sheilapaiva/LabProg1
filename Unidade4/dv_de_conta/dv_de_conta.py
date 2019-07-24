# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: DV de Conta

numero_conta = int(raw_input())
lista_numero = list(str(numero_conta))

soma_digitos = 0
for i in range(len(lista_numero)):
	soma_digitos += int(lista_numero[i])

digito_verificador = soma_digitos % 11

if digito_verificador != 10:
	print "%d-%d" % (numero_conta, digito_verificador)
else:
	print "%d-X" % (numero_conta)

