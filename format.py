  
'''
Autor:Cristina Ribeiro
Codigo: .format (como formatar strinf e printar na tela)
'''

preco = float(input('digite o preco atual do produto: '))
desconto = 5/100
print('agora o produto custa {:.2f} reais'.format(preco-(preco*desconto)))
