'''Escreva um programa que leia um arquivo de entrada contendo números inteiros, sendo um por
linha, e os coloque em uma lista. Em seguida pense em alguma forma de remover os valores
repetidos, deixando apenas uma cópia de cada valor.
A lista resultante após a eliminação dos repetidos, deve ser ordenada e salva no arquivo
UNICOS.TXT, um inteiro por linha.'''''

arq = open('NUMEROS.txt', 'r')
numeros = []

for linha in arq:
    numeros.append(int(linha.strip()))

numeros_unicos = list(set(numeros))
numeros_unicos.sort()

arq.close()

output = open('UNICOS.txt', 'w')
for numero in numeros_unicos:
    output.write(str(numero) + '\n')
output.close()

import subprocess
subprocess.run(['open', 'UNICOS.txt'])