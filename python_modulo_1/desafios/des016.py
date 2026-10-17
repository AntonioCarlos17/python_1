import math
#Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira:
num = float(input('Dígite um número real: '))
inteiro = math.floor(num)
print('A parte inteira do número {} é {}'.format(num, inteiro))
