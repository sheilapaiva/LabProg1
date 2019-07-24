# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 1 	Questão: Primeiro e Último

numero = int(raw_input())

primeiro_digito = (numero / 1000)
segundo_digito = (numero % 10)

print "%d %d" % (primeiro_digito, segundo_digito) 
