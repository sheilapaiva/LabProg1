#coding: utf-8

parte1 = int(raw_input())
parte2 = int(raw_input())
parte3 = int(raw_input())

a = (parte3 / 100)
b = ((parte3 / 10) % 10)
c = (parte3 % 10)
parte4 = (a + b + c)

print "%03.d.%03.d.%03.d-%02.d" % (parte1, parte2, parte3, parte4)
