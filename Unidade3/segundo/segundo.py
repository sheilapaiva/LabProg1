#coding: utf-8

msg = ""

num1 = int(raw_input())
num2 = int(raw_input())

msg += str(num1) + ", " + str(num2) + ", "

if num2 > num1:
	num2, num1 = num1, num2

num3 = int(raw_input())

msg += str(num3) + " e "

if num3 > num2:
	num3, num2 = num2, num3
	if num2 > num1:
		num2, num1 = num1, num2

num4 = int(raw_input())

msg += str(num4)

if num4 > num3:
	num4, num3 = num3, num4
	if num3 > num2:
		num3, num2 = num2, num3
	if num2 > num1:
		num2, num1 = num1, num2
		
print "Considerando os números " + msg
print "O segundo menor número é %d" % num3
print "O segundo maior número é %d" % num2
