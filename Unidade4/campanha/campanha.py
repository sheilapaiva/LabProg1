# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Campanha

resultado = []
lista_pontos = []
pro = 0
contra = 0
vitorias_casa = 0
derrotas_casa = 0
empates_casa = 0
vitorias_fora = 0
derrotas_fora = 0
empates_fora = 0
palavra = ""
for i in range(10):
	resultado = raw_input().split(" ")
	palavra = resultado[1]
	if palavra == "(c)":
		lista_pontos = resultado[0].split("x")
		m = int(lista_pontos[0])
		n = int(lista_pontos[1])
		pro += m
		contra += n 
		if m > n:
			vitorias_casa += 1
		elif m < n:
			derrotas_casa += 1
		else:
			empates_casa += 1
			
	if palavra == "(f)":
		lista_pontos = resultado[0].split("x")
		n = int(lista_pontos[0])
		m = int(lista_pontos[1])
		pro += m
		contra += n 
		if m > n:
			vitorias_fora += 1
		elif m < n:
			derrotas_fora += 1
		else:
			empates_fora += 1
			
vitorias = vitorias_casa + vitorias_fora
empates = empates_casa + empates_fora	
derrotas = derrotas_casa + derrotas_fora
print "%dv, %de, %dd" % (vitorias, empates, derrotas)
pontos = (((vitorias_casa + vitorias_fora) * 3) + empates)
print "pontos: %d" % pontos
saldo = pro - contra
print "saldo: %d (%d pro, %d contra)" % (saldo, pro, contra)
pontos_casa = ((vitorias_casa * 3) + empates_casa)
print "pontos em casa: %d" % pontos_casa
pontos_fora = ((vitorias_fora * 3) + empates_fora)
print "pontos fora: %d" % pontos_fora
