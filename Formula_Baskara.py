#Autor: Cristina Ribeiro
#Codigo: Calcular resultado 1 e 2 na formula de baskara


#escreva um programa que resolva equacao de segundo grau
#confirmar o resultado

from math import sqrt



elem1 = int(input('digite a base do primeiro elemento que acompanha o x: '))
elem2 = int(input('digite o segundo elemento que acompanha o x: '))
elem3 = int(input('digite o terceiro elemento da equacao: '))


print('a expressao ficou assim: \n')
print(elem1,"x²",elem2,"x",elem3,"=0")

delta = (elem2**2)-4*(elem1*(-elem3))
raizDelta = sqrt(delta)
resp1 = (-elem2 + raizDelta)/(2*elem1)
resp2 = (-elem2 - raizDelta)/(2*elem1)

print('resposta 1: ', str(resp1))
print('resposta 2: ', str(resp2))
