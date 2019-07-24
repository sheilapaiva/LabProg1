while True:
	
	lista_contador = []
	cont = 0
	binario = raw_input()

	if binario == '010101' : break

	for bit in binario:
		if bit == '1':
			cont += 1
    
		elif bit == '0' and cont != 0:
			lista_contador.append(cont)
			cont = 0
   
	if cont > 0:
	   lista_contador.append(cont)
	
	saida = ''
	for bit in range(len(lista_contador)):
		
		if bit < len(lista_contador):
			saida += str(lista_contador[bit]) + ' '
		
		elif bit == len(lista_contador) - 1:
			saida += str(lista_contador[bit])
	print saida
