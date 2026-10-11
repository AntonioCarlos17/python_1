#crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada;
num = int(input('Dígite um número qualquer: '))
dob = num * 2
trip = num * 3
raiz = num ** (1/2)
print('O número que você dígitou foi {}, o dobro dele é {}, o triplo dele é {} e a raiz quadrada é {:.4}'.format(num, dob, trip, raiz))
