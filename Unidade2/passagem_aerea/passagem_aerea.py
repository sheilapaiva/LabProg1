#coding: utf-8

distancia = float(raw_input())
aliquota = float(raw_input())

passagem = ((distancia * aliquota) + 51.00)


print "Valor da passagem: R$ %.2f\n" % passagem

print "Pagamento:"
print "1. À vista. R$ %.2f" % (passagem - (passagem * 0.25))
print "2. Em 6 parcelas. Total: R$ %.2f" % (passagem - (passagem * 0.05))
print "   6 x R$ %.2f" % ((passagem - (passagem * 0.05)) / 6)
print "3. Em 10 parcelas. Total: R$ %.2f" % passagem
print "   10 x R$ %.2f" % (passagem / 10)
