#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Unnamed

lista = []
n = ""
while True:
    if n == "fim":
        break
    quant = 0
    while True:
        n = raw_input()
        if n == "-1":
            break
        if n == "fim":
            break
        quant += 1
    lista.append(quant)
    quant = 0
maior = 0
posicao = 0
for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        posicao = i
if len(lista) > 1:
    print "Conjunto " + str(posicao + 1) + " - " + str(maior) + " elemento(s)"
else:
    n = "fim"
