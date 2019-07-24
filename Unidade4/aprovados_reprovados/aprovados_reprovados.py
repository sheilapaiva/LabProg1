#coding: utf-8

quantidade_alunos = int(raw_input())
media_alunos_reprovados = 0
media_alunos_aprovados = 0
i = 0
contar_reprovados = 0
contar_aprovados = 0
numeros = range(quantidade_alunos)

for i in numeros:
	media = float(raw_input())
	if media < 7:
		media_alunos_reprovados = media_alunos_reprovados + media
		contar_reprovados = contar_reprovados + 1 
	if media >= 7:
		media_alunos_aprovados = media_alunos_aprovados + media
		contar_aprovados = contar_aprovados + 1 

print "Reprovados: %d" % contar_reprovados
if contar_reprovados >= 1:
	print "Média: %.1f" % float(media_alunos_reprovados / contar_reprovados)

print ""
print "Aprovados: %d" % contar_aprovados
if contar_aprovados >= 1:
	print "Média: %.1f" % float(media_alunos_aprovados / contar_aprovados)
	
