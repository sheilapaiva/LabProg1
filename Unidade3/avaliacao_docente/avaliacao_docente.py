#coding: utf-8

n = int(raw_input())
pontuacao_atividades = float(raw_input())
producao_intelectual = float(raw_input())
atividades_orientacao = float(raw_input())
atividades_administrativas = float(raw_input())

if n < 4:
	print "Promoção indeferida. Número de semestres insuficiente."
	
if n >= 4:
	if pontuacao_atividades >= 320 and producao_intelectual >= 100 and atividades_orientacao >= 20:
		if atividades_administrativas < 120:
			print "Promoção indeferida. Média insuficiente."

		else:
			print "Promoção deferida. Parabéns!"
	else:
		print "Promoção indeferida. Pontuação mínima não alcançada."
