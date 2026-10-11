#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média;
nota1 = float(input('Dígite a primeira nota: '))
nota2 = float(input('Dígite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Você dígitou as notas {} e {} a média para essas notas é {}'.format(nota1, nota2, media))