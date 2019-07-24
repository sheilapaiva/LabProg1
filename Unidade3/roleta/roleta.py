#coding: utf-8

numero_aposta = int(raw_input())
cor_aposta = str(raw_input())
numero_sorteado = int(raw_input())
cor_sorteada = str(raw_input())

if numero_aposta == numero_sorteado and cor_aposta == cor_sorteada:
	print "150"

elif numero_aposta == numero_sorteado and cor_aposta != cor_sorteada:
	print "100"
	
elif numero_aposta != numero_sorteado and cor_aposta == cor_sorteada:
	if numero_sorteado > numero_aposta:
		print "80"
	if numero_sorteado < numero_aposta:
		print "100"	

else:
	print "0"

