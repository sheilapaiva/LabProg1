# coding: utf-8
# Aluna: Sheila Maria Mendes Paiva 
# Matrícula: 118210186
# Unidade 2 	Questão: Unidades e Medidas

medida_metros = float(raw_input())

centimetros = (medida_metros * 100)
polegadas = ((36 / 91.44) * centimetros)
pes = ((3 / 91.44) * centimetros)
jarda = ((1 / 91.44) * centimetros)

print "Jardas: %.3f yd" % jarda
print "Pés: %.3f ft" % pes
print "Polegadas: %.3f in" % polegadas
