# coding: utf-8
# Eleição na ADUF

abstencao = int(raw_input())
a_favor = int(raw_input())
contra = int(raw_input())

porcentagem_abstencao = float(abstencao * 100) / (abstencao + a_favor + contra)
porcentagem_favor = float(a_favor * 100) / (abstencao + a_favor + contra)
porcentagem_contra = float(contra * 100) / (abstencao + a_favor + contra)

print "Resultado da Votação"
print
print abstencao, "abstenções (%.2f%%)" % porcentagem_abstencao
print a_favor, "a favor (%.2f%%)" % porcentagem_favor
print contra, "contra (%.2f%%)" % porcentagem_contra
