# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Conta Divisíveis

numero_divisor = int(raw_input())
tamanho_sequencia = int(raw_input())

cont = 0
for i in range(tamanho_sequencia):
	numero_sequencia = float(raw_input())
	
	if numero_sequencia % numero_divisor == 0:
		cont += 1

porcetagem = ((cont * 100.) / tamanho_sequencia)

print "%d (%.1f%%)" % (cont, porcetagem)
