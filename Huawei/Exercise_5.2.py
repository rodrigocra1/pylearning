'''Escreva um programa que leia um número N e em seguida exiba na tela todos os números divisíveis
por 7 entre 1 e N (inclusive).'''

N = int(input("Digite N: "))

if N < 1:
    print("Entrada invalida")

i = 1
while i <= N:
    if i % 7 == 0:
        print(i)
        i += 1
    else:
        i += 1