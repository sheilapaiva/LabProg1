#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 4 	Questão: Coringa

coringa = int(raw_input(""))
numeros = raw_input("").split(" ")

lista = []
menor, menor2 = 0, 0
for i in range(len(numeros)):
    lista.append(int(numeros[i]))
menor = (lista[0] - coringa)

if menor < 0:
    menor = (menor * (-1))

for i in range(1,len(lista)):
    menor2 = (lista[i] - coringa)
    if menor2 < 0:
        menor2 = (menor2 * (-1))
    if menor >= menor2:
        menor = menor2
print "menor distância absoluta: %d" % menor

for i in range(len(lista)):
    if (lista[i] - coringa) == menor or ((lista[i] - coringa) * (-1) == menor):
        print "%d:%d" % (i,lista[i])
