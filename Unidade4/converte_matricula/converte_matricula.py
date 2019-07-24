# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 4 	Questão: Converte Divisíveis

matricula = raw_input()

matricula_inicial = "1"
matricula_final = ""
numero_zero = "0"
for i in range(1,5):
	matricula_inicial += matricula[i]	
matricula_final = matricula_inicial
for j in range(5, len(matricula)):
	numero_zero += matricula[j]
matricula_final += numero_zero
print matricula_final
