#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
pkm = 0.15
pdia = 60
kmpercorrido = float(input('Quantos km foi percorrido: '))
dias = int(input('Quantos dias o carro ficou alugado: '))
total = (kmpercorrido * pkm) + (dias * pdia)
print('O total a pagar é R${:.2f}'.format(total))
