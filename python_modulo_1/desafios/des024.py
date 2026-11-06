#crie um programa que leia o nome da cidade e diga se ela começa ou não com o nome 'santo'.
cid = str(input('Dígite o nome de uma cidade: '))
n = cid.lower().find('santo')
if n >= 0:
    print('O nome da Cidade começa com o nome Santo.')
else:
    print('O nome da Cidade não começa com o nome Santo.')