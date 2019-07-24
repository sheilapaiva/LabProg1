#coding: utf-8

nome = str(raw_input())
idade = int(raw_input())

if idade <= 4:
	print "%s, %d anos, Não pode competir." % (nome, idade)
if idade >= 5 and idade <= 7:
	print "%s, %d anos, Infantil A." % (nome, idade)
if idade >= 8 and idade <= 10:
	print "%s, %d anos, Infantil B." % (nome, idade)
if idade >= 11 and idade <= 13:
	print "%s, %d anos, Juvenil A." % (nome, idade)
if idade >= 14 and idade <= 17:
	print "%s, %d anos, Juvenil B." % (nome, idade)
if idade > 17:
	print "%s, %d anos, Senior." % (nome, idade)
