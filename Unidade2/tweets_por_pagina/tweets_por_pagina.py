# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 2 	Questão: Tweets por Página

quantidade_de_tweets = int(raw_input())

paginas = quantidade_de_tweets / 400
percentual_tweets = (((quantidade_de_tweets % 400) * 100.) / quantidade_de_tweets)

print "Serão necessárias %d página(s) para visualizar os tweets." % paginas
print "%.1f%% dos tweets serão perdidos." % percentual_tweets
