#coding: utf-8

media_parcial = float(raw_input())
prova_final = float(raw_input())

media_final = (((media_parcial * 60) + (prova_final * 40)) / (60 + 40))

print "Média final: %.1f" % media_final
