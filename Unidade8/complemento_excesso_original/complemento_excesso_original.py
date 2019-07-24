#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Complemento Excesso Original

#coding: utf-8
#UFCG - Ciência da Computação
#Programação I e laboratório de Programação I
#Aluna: Sheila Maria Mendes Paiva
#Unidade: 8    Questão: Complemento Excesso Original


def bits_8(string, separador):
   string_nova = ""
   for i in string:
       if i == separador:
           string_nova = ""
       else:
           string_nova += i

   resultado_final = "0" * (8 - len(string_nova)) + string_nova
   return resultado_final


def excesso_127(numero):
   numero_final = int(numero) + 127
   saida = str(bin(int(numero_final)))

   return bits_8(saida, "b")


def complemento1(numero):
   saida = str(bin(int(numero)))
   if int(numero) >= 0:
       return bits_8(saida, "b")
   else:
       saida_final = ""
       for i in bits_8(saida, "b"):
           if i == "0":
               saida_final += "1"
           else:
               saida_final += "0"

       return saida_final


while True:
   tipo = raw_input().split()
   if tipo[0] == "***":
       break
   elif tipo[0] == "C1":
       print complemento1(tipo[1])
   elif tipo[0] == "E127":
       print excesso_127(tipo[1])

