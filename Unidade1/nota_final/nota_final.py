#coding: utf-8

print "== Estágio 1 =="
peso1 = float(raw_input("Peso? "))
nota1 = float(raw_input("Nota? "))
print "== Estágio 2 =="
peso2 = float(raw_input("Peso? "))
nota2 = float(raw_input("Nota? "))
print "== Estágio 3 =="
peso3 = float(raw_input("Peso? "))
nota3 = float(raw_input("Nota? "))
print "== Resultados =="

media_parcial = float((peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3))
notafinal1 = float((5 - (media_parcial * 0.6)) / 0.4)
notafinal2 = float((7 - (media_parcial * 0.6)) / 0.4)

print "Média parcial: %.1f\nNota na final, pra média 5.0 = %.1f\nNota na final, pra média 7.0 = %.1f" % (media_parcial, notafinal1, notafinal2)
