#coding: utf-8

conta_corrente = int(raw_input())

d1 = int(conta_corrente / 10000)
d2 = int((conta_corrente / 1000) % 10)
d3 = int((conta_corrente / 100) % 10)
d4 = int((conta_corrente / 10) % 10)
d5 = int(conta_corrente % 10)
parte4 = int((d1 + d2 + d3 + d4 + d5) % 11)

print "%05.0d-%02.0d" % (conta_corrente, parte4)
