'''Escreva um programa que grave o arquivo NUMEROS.TXT com 2.000 números, um em cada linha,
gerados com a função randint() do módulo random no intervalo [1, 5.000].
VARIACAO ---
Altere este programa substituindo o tamanho fixo de 2.000 por uma quantidade de entrada a ser lida
do teclado.'''

import random
from random import randint

qty = int(input("Digite a quantidade de números a serem gerados: "))

numeros = open('NUMEROS.TXT', "w")
numlist = []
while len(numlist) < qty:
    numlist.append(randint(1, 5000))

for item in numlist:
    numeros.write(f'{item}' + '\n')
numeros.close()
for item in numlist:
    print(f'{item}')