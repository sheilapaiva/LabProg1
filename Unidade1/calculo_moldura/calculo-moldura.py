#coding: utf-8

comprimento = float(raw_input())
largura = float(raw_input())

perimetro = float(((comprimento + largura) * 2) / 100)
valor_moldura = float(perimetro * 120)

print "R$ " + str(valor_moldura)
