#coding: utf-8

num_adultos = int(raw_input())
num_criancas  = int(raw_input())
valor_ingresso = float(raw_input())

valor_total = float((valor_ingresso * num_adultos) + ((valor_ingresso * num_criancas)/2))

print "Total: R$ " + str(valor_total)
