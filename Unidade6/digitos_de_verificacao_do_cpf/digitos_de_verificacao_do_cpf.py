#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 6 	Questão: Dígitos de Verificação do CPF

def calcula_digitos_verificacao(string):
	multiplicador, digito_1 = 2, 0
	for i in range(len(string) -1, -1, -1):
		digito_1 += (int(string[i]) * multiplicador)
		multiplicador += 1
	
	resto1 = (10 * digito_1) % 11
	if resto1 == 10:
		resto1 = 0
	
	string += str(resto1)
	
	multiplicador, digito_2 = 2, 0
	for i in range(len(string) -1, -1, -1):
		digito_2 += (int(string[i]) * multiplicador)
		multiplicador += 1
	
	resto2 = (10 * digito_2) % 11
	if resto2 == 10:
		resto2 = 0
	
	verificador = str(resto1) + str(resto2)
	
	return verificador
