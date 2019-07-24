#coding: utf-8

valor_atual = float(raw_input("Valor atual? "))
novo_valor = float(raw_input("Novo valor? "))

aumento = (novo_valor - valor_atual)
percentual = ((aumento * 100) / valor_atual)

print "Reajuste de %.1f%%" % percentual
