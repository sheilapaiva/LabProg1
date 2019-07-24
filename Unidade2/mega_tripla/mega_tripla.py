#coding: utf-8

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

num1 = int(num1 % 11)
num2 = int(num2 % 11)
num3 = int(num3 % 11)

print "%02.0d-%02.0d-%02.0d" % (num1, num2, num3)
