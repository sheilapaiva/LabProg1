#coding: utf-8

custo = float(raw_input())
despesas = float(raw_input())
lucro = float(raw_input())
impostos = float(raw_input())
comissoes= float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())

desp = float((custo * despesas) / 100)
luc = float((custo * lucro) / 100)
preco_venda = float(((custo + desp + luc) * 100) / (100 - impostos - comissoes - descontos - encargos))
preco_int = int(preco_venda)
decimal = float(preco_venda - preco_int)

print "Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)" % (preco_venda, preco_int, decimal)
