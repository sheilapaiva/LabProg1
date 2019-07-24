#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 4 	Questão: B2 para B10

numero_binario = int(raw_input())
conversao = str(numero_binario)
tamanho_numero_binario = len(conversao)
lista = list(conversao)
expoente = tamanho_numero_binario - 1
numero_decimal = 0
n = 0

for i in range(tamanho_numero_binario):
	potencia = 2 ** expoente
	expoente -= 1
	num = int(lista[n])
	n += 1
	resultado = num * potencia
	numero_decimal += resultado
	
	print num, "*", potencia, "=", resultado
	
print "%d(2) = %d(10)" % (numero_binario, numero_decimal)
