#coding: utf-8
#Aluna: Sheila Maria Mendes Paiva 
#Matrícula: 118210186
#Unidade: 5 	Questão: Embarque Organizado

organizado = ""
while True:
	sequencia = raw_input().split()
	for i in range(len(sequencia)):
		if i > 0 and int(sequencia[i]) % 2 != 0 and int(sequencia[i - 1]) % 2 == 0:
			organizado = "erro"
			break
		else:
			organizado = "ok"
	break
print organizado
