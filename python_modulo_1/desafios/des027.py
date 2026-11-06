#faça um programa que leio o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#primeiro
#último
nome = str(input('Dígite seu nome completo: ')).strip()
dividido = nome.split()
print('Seu primeiro nome é {}'.format(dividido[0].title()))
print('Seu último nome é {}'.format(dividido[len(dividido)-1].title()))

