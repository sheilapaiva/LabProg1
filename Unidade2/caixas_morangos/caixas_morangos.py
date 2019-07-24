#coding: utf-8

qtd_morangos = int(raw_input())

caixas = (qtd_morangos / 400)
resto = float(qtd_morangos % 400)
perdidos = float((resto * 100) / qtd_morangos)

print "Serão necessárias %d caixa(s) para embalar os morangos." % caixas
print "%.1f%% dos morangos serão perdidos." % perdidos
