# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 1 	Questão: Divisão Safra

qtd_graos = float(raw_input())
qtd_clientes_atacado = float(raw_input())
qtd_clientes_varejo = float(raw_input())

varejo = int(qtd_graos / qtd_clientes_atacado)
a = float(qtd_graos % qtd_clientes_atacado)
atacado = float(a / qtd_clientes_varejo)
f = "%.2f" % atacado

print "Clientes no atacado = %.dkg cada." % varejo
print "Clientes no varejo = " + str(f) + "kg cada."
