#coding: utf-8

convidados = float(raw_input())

op1_inteira = int(32 / convidados)
op1_resto  = int(32 % convidados)
op2 = float(32.0 / convidados)
print 'Opção 1: %d fatias cada, %d de resto' % (op1_inteira, op1_resto)
print 'Opção 2: %.2f fatias cada' % op2
