# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 7 	Questão: Afinidade musical

def tem_afinidade(l1, l2):
	cont = 0
	for elemento_l1 in l1:
		for elemento_l2 in l2:
			if elemento_l1 == elemento_l2:
				cont += 1
	
	if cont >= 3:
		return True
	else:
		return False
			
l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True
