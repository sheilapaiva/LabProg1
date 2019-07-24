#coding: utf-8

qtd_peso = float(raw_input())
tempo = float(raw_input())
qtd_calorias = float(raw_input())

peso = float(qtd_peso * 7700)
t = float((tempo * 900) + 2000)
perda_dia = float(t - qtd_calorias)
dias = float(peso / perda_dia)

print "Você precisará de %.2f dias de dieta" % dias
