#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade 1 	Questão: Percentegem de aprovados

print "Análise da Turma"
print "==="
num_aprovados = int(raw_input("Número de aprovados? "))
num_reprovados = int(raw_input("Número de reprovados? "))
print "---"

total = (num_aprovados + num_reprovados)
percentual_aprovados = ((num_aprovados * 100.0) / total)
percentual_reprovados = ((num_reprovados * 100.0) / total)

print "Total de alunos na turma: %d" % total
print "Aprovados: %d = %.1f%%" % (num_aprovados, percentual_aprovados)
print "Reprovados: %d = %.1f%%" % (num_reprovados, percentual_reprovados)
