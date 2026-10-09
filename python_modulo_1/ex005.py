n1 = int(input('Digite um valor: '))
n2 = int(input('digite um segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' A soma dos numero {} e {} é {}, a multiplicação é {}, é a divisão é {:.3}'.format(n1, n2, s, m, d), end='')
print(' A divisão inteira entre os números {} e {} é {}, e a potência é {}'.format(n1, n2, di, e))

# \n a linha quebra onde colocar
# end=' ' evita a quebra de linha e coloca toda a informação em uma linha só
