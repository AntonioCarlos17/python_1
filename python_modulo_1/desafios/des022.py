#crie um programa que leia o nome completo da pessoa e mostre na tela:
#o nome com todas as letras maiúsculas
#o nome com todas as letras minúsculas
#quantas letras ao todo sem considerar espaços
#quantas letras tem o primeiro nome.
nome = str(input("Dígite seu nome completo: ")).strip()
mai = nome.upper()
print('nome com todas as letras maiúsculas: {}'.format(mai))
min = nome.lower()
print('nome com todas as letras minúsculas: {}'.format(min))
dividido = nome.split()
print('A quantidade de letras no nome é: {}'.format((len(nome)-nome.count(' '))))
print('A quantidade de letras no primeiro nome é: {}'.format(len(dividido[0])))
