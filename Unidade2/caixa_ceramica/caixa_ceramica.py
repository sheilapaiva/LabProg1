#coding: utf-8

capacidade = float(raw_input("Capacidade de revestimento? "))
print ""

print "== Dados do vão a revestir =="
comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura? "))

lateral1 = float(2 * (comprimento * altura))
lateral2 = float(2 * (largura * altura))
base = float(comprimento * largura)
area_total = float(lateral1 + lateral2 + base)
num_caixas = int(area_total / capacidade)

print ""
print "== Resultados =="
print "Área total a revestir: %.1f m2" % area_total
print "Número de caixas: %d" % num_caixas
