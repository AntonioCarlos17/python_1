import math
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno. conseno e da tangente desse ângulo.
angulo = int(input('Dígite o valor de um angulo que você queira saber o seno, coseno e a tangente: '))
radios = math.radians(angulo)
seno = math.sin(radios)
coseno = math.cos(radios)
tangente = math.tan(radios)
print('O angulo que você dígitou é {} \n'
      'possui o seno {} \n'
      'possui o coseno {} \n'
      'e possui a tangente {}'.format(angulo, seno, coseno, tangente))