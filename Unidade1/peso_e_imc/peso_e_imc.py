# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 1 	Questão: Peso e IMC

peso = float(raw_input())
altura = float(raw_input())

imc = peso / altura ** 2
peso_ideal = ((24.9 * (altura ** 2)) - peso)

print "IMC atual = %.2f" % imc
print "Peso a ser ganho/perdido = %.2f" % peso_ideal
