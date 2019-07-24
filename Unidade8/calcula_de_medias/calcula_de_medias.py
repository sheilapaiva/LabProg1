#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Calculadora de Médias


def media_aritmetica(lista_valores):
	media = 0.0
	for i in range(len(lista_valores)):
		media += float(lista_valores[i]) / len(lista_valores)
	print "Média Aritmética: %.4f" % media
	return media
	
	
def media_geometrica(lista_valores):
	media = 1.0
	for i in range(len(lista_valores)):
		media *= float(lista_valores[i]) ** float(1.0/len(lista_valores))
	print "Média Geométrica: %.4f" % media
	return media
	
	
def media_harmonica(lista_valores):
	soma = 0.0
	for i in range(len(lista_valores)):
		soma += (1.0/float(lista_valores[i]))
	media = len(lista_valores) / soma 
	print "Média Harmônica: %.4f" % media
	return media


while True:
	tipo_media = raw_input().split()
	if tipo_media[0] == "Q":
		break
	else:
		valores = raw_input().split()
		for i in range(len(tipo_media)):
			if tipo_media[i] == "MA":
				media_aritmetica(valores)
			elif tipo_media[i] == "MG":
				media_geometrica(valores)
			elif tipo_media[i] == "MH":
				media_harmonica(valores)
		print "----"
			
