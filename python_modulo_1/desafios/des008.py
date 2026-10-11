# escreva um programa que leia um valor em metros e exiba-os em convertidos para centímetros e milímetros.
num = float(input('Dígite os metros para conversão: '))
cent = num * 100
mili = num * 1000
print('Você digitou {}, a conversão em centimetros é {} e a conversão em milimetros é {}.'.format(num, cent, mili))