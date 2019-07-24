#coding: utf-8

s_inicial = float(raw_input())
velocidade = float(raw_input())
t = float(raw_input())

posicao_final = float(s_inicial + (velocidade * t))

print "Posição final do móvel"
print "S(%.1f) = %.1f m" % (t, posicao_final)
