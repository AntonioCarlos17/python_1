#feça um programa que leia uma frase qualquer pelo teclado e mostre:
#quantas vezes aparece a letra A.
#em que posição ela aparece a primeira vez
#em que posição ela apara a última vez
frase = str(input('Dígite uma frase: ')).upper().strip()
print('A letra "A" apareceu {}'.format(frase.count('A')))
print('A letra "A" apareceu a primeira vez na posição {}'.format(frase.find('A')+1))
print('A última vez que a letra "A" apareceu foi na posição {}'.format(frase.rfind('A')+1))

