'''Escreva um programa que permaneça em laço lendo do teclado números inteiros entre 1 e 9. Outros
valores devem ser ignorados. Esse laço termina quando for digitado zero ou qualquer valor negativo.
O objetivo deste programa é contar quantas vezes cada valor entre 1 e 9 foi digitado.
Ao término do laço de leitura o programa deve mostrar quais valores foram digitados e quantas vezes
cada um. Obrigatoriamente use um dicionário.'''

dictNumbers = {}
while True:
    number = int(input('Digite um número de 1 a 9: '))

    if number == 0 or number < 0:
        print(dictNumbers)
        break

    elif number <= 9 and number >= 1:
        if number in dictNumbers:
            dictNumbers[number] += 1
        else:
            dictNumbers[number] = 1

    else:
        print('Error - digite um numero de 1 a 9...')

print('Resumo das entradas: ')
for items in dictNumbers.items():
    print(f'\nO número {items[0]} foi digitado {items[1]} vezes!')

