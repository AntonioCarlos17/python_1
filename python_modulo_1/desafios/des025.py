#crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.
nome = str(input('Dígite seu nome completo: '))
nom = nome.lower().find('silva')
if nom >= 0 :
    print('O nome digitado tem silva nele')
else:
    print('O nome digitado não tem o nome silva.')