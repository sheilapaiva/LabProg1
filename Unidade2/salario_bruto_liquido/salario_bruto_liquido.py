
#coding: utf-8

nome = str(raw_input())
qtd_horas_extras = float(raw_input())
valor_salario_minimo = float(raw_input())
valor_hora_extra = float(raw_input())

salario_hora_extra =  (qtd_horas_extras * valor_hora_extra)
salario_bruto = (4 * valor_salario_minimo + salario_hora_extra)
desconto_inss = (salario_bruto * 0.12)
desconto_imposto_renda = (salario_bruto * 0.20)
desconto = (desconto_imposto_renda + desconto_inss)
salario_liquido = (salario_bruto - desconto)

print "O Salário Bruto de %s é de R$ %.2f" % (nome, salario_bruto)
print "O Salário Líquido de %s é de R$ %.2f" % (nome, salario_liquido) 
