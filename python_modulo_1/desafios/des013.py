# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Dígite seu sálario atual: '))
aumento = 0.15
novo = salario * aumento
final = salario + novo
print('O seu antigo sálario era R${}.\n'
      'Foi adicionado um aumento de R${}.\n'
      'O seu novo sálario a receber é de R${}'.format(salario, novo, final))