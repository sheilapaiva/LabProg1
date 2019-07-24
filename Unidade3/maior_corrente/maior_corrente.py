#coding: utf-8

tensao1 = int(raw_input())
resistencia1 = float(raw_input())
tensao2 = int(raw_input())
resistencia2 = float(raw_input())
tensao3 = int(raw_input())
resistencia3 = float(raw_input())

corrente1 = tensao1 / resistencia1
corrente2 = tensao2 / resistencia2
corrente3 = tensao3 / resistencia3

if corrente1 > corrente2 and corrente1 > corrente3:
	print "condutor com maior corrente: 1"
	if corrente1 >= 1:
		print "maior corrente: %.2f A" % corrente1
	if corrente1 < 1 and corrente1 > 0.001:
		corrente1 = corrente1 * 1000
		print "maior corrente: %.2f mA" % corrente1
	if corrente1 <= 0.001:
		corrente1 = (corrente1 * 1000) * 1000
		print "maior corrente: %.2f µA" % corrente1
	
if corrente2 > corrente1 and corrente2 > corrente3:
	print "condutor com maior corrente: 2"
	if corrente2 >= 1:
		print "maior corrente: %.2f A" % corrente2
	if corrente2 < 1 and corrente2 > 0.001:
		corrente2 = corrente2 * 1000
		print "maior corrente: %.2f mA" % corrente2
	if corrente2 <= 0.001:
		corrente2 = (corrente2 * 1000) * 1000
		print "maior corrente: %.2f µA" % corrente2
	
if corrente3 > corrente1 and corrente3 > corrente2:
	print "condutor com maior corrente: 3"
	if corrente3 >= 1:
		print "maior corrente: %.2f A" % corrente3
	if corrente3 < 1 and corrente3 > 0.001:
		corrente3 = corrente3 * 1000
		print "maior corrente: %.2f mA" % corrente3
	if corrente3 <= 0.001:
		corrente3 = (corrente3 * 1000) * 1000
		print "maior corrente: %.2f µA" % corrente3
	
if corrente1 == corrente2 and corrente1 > corrente3 or corrente1 == corrente3 and corrente1 > corrente2:
	print "condutor com maior corrente: 1"
	if corrente1 >= 1:
		print "maior corrente: %.2f A" % corrente1
	if corrente1 < 1 and corrente1 > 0.001:
		corrente1 = corrente1 * 1000
		print "maior corrente: %.2f mA" % corrente1
	if corrente1 <= 0.001:
		corrente1 = (corrente1 * 1000) * 1000
		print "maior corrente: %.2f µA" % corrente1
			

if corrente2 == corrente3 and corrente2 > corrente1:
	print "condutor com maior corrente: 2"
	if corrente2 >= 1:
		print "maior corrente: %.2f A" % corrente2
	if corrente2 < 1 and corrente2 > 0.001:
		corrente2 = corrente2 * 1000
		print "maior corrente: %.2f mA" % corrente2
	if corrente2 <= 0.001:
		corrente2 = (corrente2 * 1000) * 1000
		print "maior corrente: %.2f µA" % corrente2
		
		
		
