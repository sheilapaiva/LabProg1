#coding: utf-8

quantidade_km = float(raw_input())
tempo = float(raw_input())

velocidade = (quantidade_km / tempo)

if (velocidade < 10.0):
	print "Velocidade: %.1fkm/h. Corredor amador." % velocidade

if (velocidade >= 10.0) and (velocidade <= 15.0):
	print "Velocidade: %.1fkm/h. Corredor aspirante." % velocidade
	
if (velocidade > 15.0):
	print "Velocidade: %.1fkm/h. Corredor profissional." % velocidade
