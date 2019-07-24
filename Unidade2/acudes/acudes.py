#coding: utf-8

capacidade = float(raw_input("capacidade? "))
percentual = float(raw_input("percentual hoje? "))
gasto = float(raw_input("gasto diário? "))

volume = float((capacidade * percentual) / 100)
dias = int(volume / gasto)

print "volume: %.2f" % volume
print "dias restantes: %d" % dias
