# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Forma Palavra (qualitativa)

palavra1 = raw_input()
palavra2 = raw_input()
palavra3 = raw_input()

palavra_nova = ""
for i in range(len(palavra1)):
	posicao_palavra1 = palavra1[i]
	posicao_palavra2 = palavra2[i]
	posicao_palavra3 = palavra3[i]
	if posicao_palavra1 <= posicao_palavra2 < posicao_palavra3:
		palavra_nova += posicao_palavra3
	elif posicao_palavra2 <= posicao_palavra1 < posicao_palavra3:
		palavra_nova += posicao_palavra3	
	elif posicao_palavra1 <= posicao_palavra3 < posicao_palavra2:
		palavra_nova += posicao_palavra2
	elif posicao_palavra3 <= posicao_palavra1 < posicao_palavra2:
		palavra_nova += posicao_palavra2	
	elif posicao_palavra2 <= posicao_palavra3 < posicao_palavra1:
		palavra_nova += posicao_palavra1
	elif posicao_palavra3 <= posicao_palavra2 < posicao_palavra1:
		palavra_nova += posicao_palavra1
	elif posicao_palavra1 == posicao_palavra2 < posicao_palavra3:
		palavra_nova += posicao_palavra3
	elif posicao_palavra1 == posicao_palavra2 > posicao_palavra3:
		palavra_nova += posicao_palavra1
	elif posicao_palavra1 == posicao_palavra3 < posicao_palavra2:
		palavra_nova += posicao_palavra2
	elif posicao_palavra1 == posicao_palavra3 > posicao_palavra2:
		palavra_nova += posicao_palavra1
	elif posicao_palavra2 == posicao_palavra3 < posicao_palavra1:
		palavra_nova += posicao_palavra1
	elif posicao_palavra2 == posicao_palavra3 > posicao_palavra1:
		palavra_nova += posicao_palavra2
	elif posicao_palavra2 == posicao_palavra3 == posicao_palavra1:
		palavra_nova += posicao_palavra1
print palavra_nova
