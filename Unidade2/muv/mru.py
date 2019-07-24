#coding: utf-8

posicao_inicial = float(raw_input("Posição inicial? "))
velocidade_inicial = float(raw_input("Velocidade inicial? "))
tempo = float(raw_input("Tempo? "))
aceleracao = float(raw_input("Aceleração? "))

v = (velocidade_inicial + (aceleracao * tempo))
vm = ((velocidade_inicial + v) / 2)
s = (posicao_inicial + (velocidade_inicial * tempo) + ((aceleracao * tempo ** 2) / 2))

print "\nDados da questão"
print "================"
print "   Posição inicial: %.2f m" % posicao_inicial
print "Velocidade inicial: %.2f m/s" % velocidade_inicial
print "        Aceleração: %.2f m/s2" % aceleracao
print "             Tempo: %.2f s" % tempo
print "  Velocidade final: %.2f m/s" % v
print "  Velocidade média: %.2f m/s" % vm
print "     Posição final: %.2f m" % s
