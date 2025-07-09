'''Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com
3 casas decimais. Usar o méthodo .write()'''

arq = open('saida_er_11.2.txt', 'w')

A = float(input('Digite um real:  '))

while A != 0:
    arq.write(f'{A:.3f}\n')
    A = float(input('Digite um real:  '))

arq.close()