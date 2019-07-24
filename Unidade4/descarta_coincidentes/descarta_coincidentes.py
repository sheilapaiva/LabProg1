# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Descarta coincidentes

sequencia_numeros = int(raw_input())

msg_descartados = ""
msg_aceitos = ""
cont_descartados = 0
cont_aceitos = 0
for i in range(sequencia_numeros):
	numero = raw_input()
	posicao = 0
	condicao_parada = 0
	
	for j in range(len(numero)):
		posicao = int(numero[j])
		if posicao == j and condicao_parada == 0:
			cont_descartados += 1
			msg_descartados += "\n" + numero
			condicao_parada = 1
	if condicao_parada == 0:
		cont_aceitos += 1
		msg_aceitos += "\n" + numero
	
print "---"
print "%d aceito(s)%s" % (cont_aceitos, msg_aceitos)
print "%d descartado(s)%s" % (cont_descartados, msg_descartados)
