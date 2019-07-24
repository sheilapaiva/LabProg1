#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Limite açude

limite_superior = float(raw_input())
nivel_atual = float(raw_input())

while nivel_atual < limite_superior:
	sequencia_operacao = raw_input().split()
	operacao = sequencia_operacao[0]
	nivel = float(sequencia_operacao[1])
	
	if operacao == "chuva":
		nivel_atual += nivel
	if operacao == "afluente":
		nivel_atual += nivel
	if operacao == "demanda" and (nivel_atual - nivel) >= 0:
		nivel_atual -= nivel
		
print "Açude passou a liberar água."
print "Nível: %.2f" % nivel_atual
