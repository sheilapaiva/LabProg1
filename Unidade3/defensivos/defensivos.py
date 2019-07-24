#coding: utf-8

produto = str(raw_input())
area = float(raw_input())

quantidade_fungicida1 = ((area * 1) / 50)
quantidade_fungicida2 = (((area * 1) / 50) + 1)
quantidade_inseticida1 = ((area * 2.5) / 30)
quantidade_inseticida2 = (((area * 2.5) / 30) + 1)
quantidade_herbicida1 = ((area * 0.3) / 1)
quantidade_herbicida2 = (((area * 0.3) / 1) + 1)
valor_fungicida = ((int(quantidade_fungicida1) + 1) * 320)
valor_inseticida = ((int(quantidade_inseticida1) + 1) * 400)
valor_herbicida = ((int(quantidade_herbicida1) + 1) * 100)

if produto == "Fungicida" or produto == "fungicida":
	if quantidade_fungicida1 <= 0 or quantidade_fungicida1 % 1 != 0:
		print "%d Fungicida(s). %.2f reais." % (quantidade_fungicida2, valor_fungicida)
	else:
		print "%d Fungicida(s). %.2f reais." % (quantidade_fungicida1, (valor_fungicida - 320))

if produto == "Inseticida" or produto == "inseticida":
	if quantidade_inseticida1 <= 0 or quantidade_inseticida1 % 1 != 0:
		print "%d Inseticida(s). %.2f reais." % (quantidade_inseticida2, valor_inseticida)
	else:
		print "%d Inseticida(s). %.2f reais." % (quantidade_inseticida1, valor_inseticida - 400)

if produto == "Herbicida" or produto == "herbicida":
	if quantidade_herbicida1 <= 0 or quantidade_herbicida1 % 1 != 0: 
		print "%d Herbicida(s). %.2f reais." % (quantidade_herbicida2, valor_herbicida)
	else:
		print "%d Herbicida(s). %.2f reais." % (quantidade_herbicida1, valor_herbicida - 100)
