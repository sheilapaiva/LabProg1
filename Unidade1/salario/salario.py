# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 1 	Questão: Salário

salario_bruto = float(raw_input())
horas_de_trabalho = int(raw_input())

hora_bruta = salario_bruto / horas_de_trabalho
desconto_imposto_renda = ((salario_bruto * 11) / 100)
desconto_inss = ((salario_bruto * 8) / 100)
desconto_sindicato = ((salario_bruto * 5) / 100)
salario_liquido = (salario_bruto - desconto_imposto_renda - desconto_inss - desconto_sindicato)
hora_liquida = salario_liquido / horas_de_trabalho

print "Salário Bruto = %.1f" % salario_bruto
print "Hora Bruta = " + str(hora_bruta)
print "Desconto IR = %.1f" % desconto_imposto_renda
print "Desconto INSS = %.1f" % desconto_inss
print "Desconto Sindicato = %.1f" % desconto_sindicato
print "Salário Líquido = %.1f" % salario_liquido
print "Hora Líquida = " + str(hora_liquida)
