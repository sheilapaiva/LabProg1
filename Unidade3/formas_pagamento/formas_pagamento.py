#coding: utf-8

area_construida = float(raw_input())
valor_metro = float(raw_input())
opcao_pagamento = str(raw_input())

iptu = (area_construida * valor_metro)

if opcao_pagamento == "vista":
	iptu = (iptu - (iptu * 0.2))
	print "Total: R$ %.2f" % iptu
	
if opcao_pagamento == "2x":
	iptu = (iptu - (iptu * 0.1))
	parcelas = (iptu / 2.)
	print "Total: R$ %.2f. Parcelas: R$ %.2f" % (iptu, parcelas)
	
if opcao_pagamento == "3x":
	iptu = (iptu - (iptu * 0.05))
	parcelas = (iptu / 3.)
	print "Total: R$ %.2f. Parcelas: R$ %.2f" % (iptu, parcelas)
