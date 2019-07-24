# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Acima da média

media_mensal = float(raw_input()) 

lista = []
while True:
    linha = raw_input() 
    dados = linha.split()
    
    media_diaria = 0.0 
    for i in range(len(dados)):
        if dados[i] == "fim": 
			break 
        dados[i] = int(dados[i])
        media_diaria += dados[i]
    
    media_diaria /= len(dados)
    if media_diaria * 2 < media_mensal:
        break
    elif media_diaria > media_mensal:
       lista.append(linha)

for k in range(len(lista)): 
    print(lista[k])
