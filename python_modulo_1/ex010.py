#nome = str(input('Dígite seu nome: ')).strip().lower()
#if nome == 'gustavo':
#     print('que nome bobo você tem:')
#print('bom dia {}'.format(nome))
nota1 = float(input('Dígite a primeira nota: '))
nota2 = float(input('Dígite a segunda nota: '))
m = (nota1 + nota2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, PARABÉNS!')
else:
    print('Sua média não foi boa, estude mais')
