# Faça um programa que leia a largura e a altura de uma parede em metros, cálcule a sua área e a quantidade de tinta
# necessária para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2 m2.
lar = float(input('Dígite a Largura da parede: '))
alt = float(input('Dígite a altura da parede: '))
area = alt * lar
tinta = area / 2
print('Pela altura e largura apresentados, deu uma area total de {}.\n Você precisará de {} litro(s) de tinta para pintar'
      ' a parede.'.format(area, tinta))