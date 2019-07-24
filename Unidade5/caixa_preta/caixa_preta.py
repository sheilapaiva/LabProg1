#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Caixa Preta (descartando leituras)

contar_peso, contar_combustivel, contar_altitude = 0,0,0
while True:
	lista = raw_input().split(" ")
	peso = int(lista[0])
	combustivel = int(lista[1])
	altitude = int(lista[2])
	
	if peso >= 0:
		contar_peso += 1
	else:
		print "dado inconsistente. peso negativo."
		break
	if combustivel >= 0:
		contar_combustivel += 1
	else:
		print "dado inconsistente. combustível negativo."
		break
	if altitude >= 0:
		contar_altitude += 1
	else:
		print "dado inconsistente. altitude negativa."
		break

print "peso: %d" % contar_peso
print "combustível: %d" % contar_combustivel
print "altitude: %d" % contar_altitude

