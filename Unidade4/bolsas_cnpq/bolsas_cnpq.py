#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade 4 	Questão: Bolsas do CNPq

saldo_temporario = 0
saldo = 0
mes_com_maior_saldo = 0

for i in range(12):
	gasto_mes = int(raw_input())
	saldo = ((saldo + 500) - gasto_mes)
		
	if saldo >= saldo_temporario:
		saldo_temporario = saldo
		mes_com_maior_saldo = i
		
if mes_com_maior_saldo == 0:
	print "jan"

elif mes_com_maior_saldo == 1:
	print "fev"

elif mes_com_maior_saldo == 2:
	print "mar"

elif mes_com_maior_saldo == 3:
	print "abr"

elif mes_com_maior_saldo == 4:
	print "mai"
	
elif mes_com_maior_saldo == 5:
	print "jun"

elif mes_com_maior_saldo == 6:
	print "jul"

elif mes_com_maior_saldo == 7:
	print "ago"

elif mes_com_maior_saldo == 8:
	print "set"
	
elif mes_com_maior_saldo == 9:
	print "out"
	
elif mes_com_maior_saldo == 10:
	print "nov"

elif mes_com_maior_saldo == 11:
	print "dez"
