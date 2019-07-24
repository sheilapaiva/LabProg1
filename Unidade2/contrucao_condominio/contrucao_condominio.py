#coding: utf-8

primeiro_lado = float(raw_input())
segundo_lado = float(raw_input())
area_casa = float(raw_input())

area_terreno = (primeiro_lado * segundo_lado)
qtd_casas = (area_terreno / area_casa)

print "%d casa(s) pode(m) ser construída(s) no terreno." % qtd_casas
