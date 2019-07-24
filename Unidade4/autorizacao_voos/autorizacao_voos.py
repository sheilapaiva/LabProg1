#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 4 	Questão: Autorização voos

tempo = int(raw_input())
quantidade_avioes = int(raw_input())
autorizado = 0

for i in range(quantidade_avioes):
	tempo_decolagem_aviao = int(raw_input())
	
	if tempo_decolagem_aviao <= tempo:
		tempo = (tempo - tempo_decolagem_aviao)
		autorizado += 1
	
print "%d voo(s) autorizados." % autorizado
