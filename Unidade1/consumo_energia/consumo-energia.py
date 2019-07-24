# coding: utf-8
# Calculando o consumo de energia em Joules

potencia = float(raw_input())
tempo = float(raw_input())
potencia_convertida = float(potencia / 1000)
tempo_convertido = float(tempo / 60)

print str(potencia_convertida * tempo_convertido) + ' kWh'
