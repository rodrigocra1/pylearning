'''Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha.
Usar o mét odo .write()'''

arq = open('saida_er_11.1.txt', 'w')

A = int(input('Digite um inteiro:  '))

while A != 0:
    arq.write(f'{A}\n')
    A = int(input('Digite um inteiro:  '))

arq.close()