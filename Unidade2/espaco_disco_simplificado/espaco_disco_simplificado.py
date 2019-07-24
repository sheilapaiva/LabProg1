#coding: utf-8

nome1 = raw_input()
espaco1 = float(raw_input())
nome2 = raw_input()
espaco2 = float(raw_input())
nome3 = raw_input()
espaco3 = float(raw_input())

espaco_utilizado1 = float((espaco1 / 1024) / 1024)
espaco_utilizado2 = float((espaco2 / 1024) / 1024)
espaco_utilizado3 = float((espaco3 / 1024) / 1024)

print "SPLab - Espaço utilizado pelos usuários"
print "---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado"
print ""

print "1, %s, %.2f MB" % (nome1, espaco_utilizado1)
print "2, %s, %.2f MB" % (nome2, espaco_utilizado2)
print "3, %s, %.2f MB" % (nome3, espaco_utilizado3)

espaco_total = float(espaco_utilizado1 + espaco_utilizado2 + espaco_utilizado3)
espaco_medio = float(espaco_total / 3)

print ""
print "Espaço total ocupado: %.2f MB" % espaco_total
print "Espaço médio ocupado: %.2f MB" % espaco_medio
