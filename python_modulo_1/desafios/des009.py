#faça um programa que leia um número qualquer e mostre a sua tabuada;
num = int(input('Dígite um número qualquer para saber a sua tabuada: '))
x = 0
while x < 11:
    tab = num * x
    print('{} X {} = {}'.format(num, x, tab))
    x += 1
