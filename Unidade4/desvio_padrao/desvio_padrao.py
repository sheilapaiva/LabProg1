# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Desvio Padrão

import math

sequencia1 = list(raw_input().split(" "))
tamanho_sequencia1 = len(sequencia1)
sequencia2 = list(raw_input().split(" "))
tamanho_sequencia2 = len(sequencia2)

#Desvio padrão sequência 1
media_sequencia1 = 0
for i in range(len(sequencia1)):
	 media_sequencia1 += (float(sequencia1[i]) / tamanho_sequencia1)
diferenca_sequencia1 = 0
for j in range(len(sequencia1)):
	diferenca_sequencia1 += ((float(sequencia1[j]) - media_sequencia1) ** 2)
desvio_sequencia1 = math.sqrt(diferenca_sequencia1 / (tamanho_sequencia1 - 1))

#Desvio padrão sequência 2
media_sequencia2 = 0
for i in range(len(sequencia2)):
	 media_sequencia2 += (float(sequencia2[i]) / tamanho_sequencia2)
diferenca_sequencia2 = 0
for j in range(len(sequencia2)):
	diferenca_sequencia2 += ((float(sequencia2[j]) - media_sequencia2) ** 2)
desvio_sequencia2 = math.sqrt(diferenca_sequencia2 / (tamanho_sequencia2 - 1))

#Comparação dos desvios padrão
if desvio_sequencia1 > desvio_sequencia2:
	print "A sequência 1 possui o maior desvio padrão (%.2f)." % desvio_sequencia1
elif desvio_sequencia2 > desvio_sequencia1:
	print "A sequência 2 possui o maior desvio padrão (%.2f)." % desvio_sequencia2
else:
	print "As sequências possuem o mesmo desvio padrão (%.2f)." % desvio_sequencia1
