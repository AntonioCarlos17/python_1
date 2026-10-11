# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$1,00 = R$3,27
real = 3.27
carteira = float(input('Dígite quanto você tem na conta: '))
dolar = carteira / real
print('Olá! \n Você consegue comprar {:.6} dólares com o dinheiro em reais que você tem na conta.'.format(dolar))
