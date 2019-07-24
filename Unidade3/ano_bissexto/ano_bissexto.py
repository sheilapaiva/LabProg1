#coding: utf-8

num = float(raw_input())

if num % 400 == 0:
	print "%d é bissexto" % num
elif num % 4 == 0 and num % 100 != 0:
	print "%d é bissexto" % num
else:
	print "%d não é bissexto" % num
