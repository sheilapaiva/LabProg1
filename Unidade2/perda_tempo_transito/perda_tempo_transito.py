#coding: utf-8

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())
num4 = int(raw_input())
num5 = int(raw_input())

minutos_perdidos = (num1 + num2 + num3 + num4 + num5)
media_minutos_perdidos = ((num1 + num2 + num3 + num4 + num5) / 5.0)
produtividade = ((minutos_perdidos * 100.0) / (120.0 * 60.0))
episodios = (minutos_perdidos / 50)

print "Você perdeu %d min na semana (média de %.1f min por dia)." % (minutos_perdidos, media_minutos_perdidos)
print "Isso significa %.2f%% da sua semana produtiva." % produtividade
print "Daria para assistir %d episódio(s) de House." % episodios
