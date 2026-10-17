import random
#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa pra ele, lendo um nome deles
# e escrevendo o  nome escolhido
nome = []
x = 0
while x < 4:
    nome.append(input('Dígite um nome: '))
    x += 1
vencedor = random.choice(nome)
print('O vencedor é: {}'.format(vencedor))