import random
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia os nomes dos quatro alunos e mostre a ordem sorteada.
nome = []
x = 0
while x < 4:
    nome.append(input('Dígite um nome: '))
    x +=1
random.shuffle(nome)
print(nome)

