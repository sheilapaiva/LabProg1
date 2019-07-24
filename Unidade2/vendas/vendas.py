#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 2    Questão: Vendas

brinquedos_vendidos_loja = int(raw_input())
brinquedos_vendidos_teresa = int(raw_input())
brinquedos_vendidos_carla = int(raw_input())

brinquedos_vendidos_joaquim = (brinquedos_vendidos_loja - (brinquedos_vendidos_teresa + brinquedos_vendidos_carla))

print "Teresa vendeu %d (de %d) brinquedos. (%.2f%%)" % (brinquedos_vendidos_teresa, brinquedos_vendidos_loja, ((brinquedos_vendidos_teresa * 100.0) / brinquedos_vendidos_loja))
print "Joaquim vendeu %d (de %d) brinquedos. (%.2f%%)" % (brinquedos_vendidos_joaquim, brinquedos_vendidos_loja, ((brinquedos_vendidos_joaquim * 100.0) / brinquedos_vendidos_loja))
print "Carla vendeu %d (de %d) brinquedos. (%.2f%%)" % (brinquedos_vendidos_carla, brinquedos_vendidos_loja, ((brinquedos_vendidos_carla * 100.0) / brinquedos_vendidos_loja))
