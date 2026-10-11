# Faça um algoritmo  que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
produto = float(input('Dígite o preço atual do produto: '))
desconto = 0.05
sub = produto * desconto
preço = produto - sub
print('O preço informado foi {},\n'
      ' após aplicar o desconte de 5%,\n'
      ' o valor atual do produto é {:.4}'.format(produto, preço))