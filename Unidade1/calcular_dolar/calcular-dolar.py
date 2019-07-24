#coding: utf-8

valor_real = float(raw_input("Reais? "))
valor_cotacao = float(raw_input("Cotação? "))

valor_dolar = float(valor_real * valor_cotacao)

print "Conversão: $ " + str(valor_dolar)
