#coding: utf-8

area = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))

iptu = float((area * aliquota) + 35.00)
unica = float(iptu - (iptu * 0.25))
desconto = float(iptu - (iptu * 0.05))
parcela_6 = float(desconto / 6)
parcela_10 = float(iptu / 10)

print "IPTU: R$ %.2f\n" % iptu
print "Pagamento:"
print "1. Quota única. R$ %.2f" % unica
print "2. Em 6 parcelas. Total: R$ %.2f" % desconto
print "   6 x R$ %.2f" % parcela_6
print "3. Em 10 parcelas. Total: R$ %.2f" % iptu
print "   10 x R$ %.2f" % parcela_10
