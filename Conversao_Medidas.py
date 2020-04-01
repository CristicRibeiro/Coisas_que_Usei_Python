'''
Autor:Cristina Ribeiro
Codigo: converter numero em metros, centimetros e milimetros
'''


metros = float(input('digite o valor a ser convertido: '))
cm = metros*100
mm = metros*1000

#dentro de {} será preenchido com a variavel que estiver depois de .format - dentro do parentese
print('{:.0f} centimetros eh equivalente a {} metros'.format(cm, metros))
print('{:.0f} mm eh equivalente a {} metros'.format(mm, metros))
