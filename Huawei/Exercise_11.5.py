'''Escreva um programa que leia o arquivo NUMEROS.TXT gerado no exercício proposto 11.4,
colocando-os em uma lista. Ordene a lista usando o .sort() e grave os números ordenados no arquivo
ORDENADOS.TXT.'''

numeros = open('NUMEROS.TXT', 'r')
numerosList = []
for linhas in numeros:
    numerosList.append(int(linhas.strip()))
numerosList.sort()
numeros.close()

print(numerosList)

ordenados = open('ORDENADOS.TXT', 'w')

for item in numerosList:
    ordenados.write(f'{item}' + '\n')
ordenados.close()