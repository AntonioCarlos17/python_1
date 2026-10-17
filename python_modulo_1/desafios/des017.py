import math
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.
oposto = float(input('Dígite o cateto oposto: '))
adjacente = float(input('Dígite o cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('A hipotenusa dos valores passados é {}'.format(hipotenusa))
