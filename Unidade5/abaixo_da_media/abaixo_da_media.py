# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 5 	Questão: Abaixo da média

tamanho = []
while True:
    linha = raw_input()
    if linha == "fim": 
		break
    tamanho.append(linha)
   
media = 0.0 
for i in range(len(tamanho)):
    tamanho[i] = int(tamanho[i])
    media += tamanho[i]
media = media / len(tamanho)
print "%.2f" % media

for j in range(len(tamanho)):
	if tamanho[j] < media:
		print "%d %s" % (j + 1, tamanho[j])
