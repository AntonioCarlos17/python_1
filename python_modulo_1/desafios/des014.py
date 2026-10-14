# escreva um programa que convertar a temperatura digitada em ºC e converta para ºF

c = float(input('Informe a temperauta em ºC para converter: '))
f=( ( 9 * c ) / 5 ) + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))