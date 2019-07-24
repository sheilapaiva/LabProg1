#coding: utf-8

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

somatorio = (num1 + num2 + num3)

if somatorio % 3 == 0 and somatorio % 5 == 0:
	print "plifplof"

elif somatorio % 5 == 0:
	print "plof"
	
elif somatorio % 3 == 0:
	print "plif"
	
else: 
	print somatorio
