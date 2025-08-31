'''Escreva um programa que leia do teclado um número inteiro D. Esse número deve ser
obrigatoriamente maior que zero. Em seguida exiba na tela todos os números inteiros menores que
100 e que sejam divisíveis por D.'''

D = int(input("Digite um numero inteiro: "))

if D <= 0:
    print("Numero deve ser maior que 0")

else:
    i = 1
    while i < 100:
        if i % D == 0:
            print(i)
        i = i + 1