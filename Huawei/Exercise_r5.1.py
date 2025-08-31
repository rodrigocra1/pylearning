'''Escreva um programa que permaneça em laço enquanto um valor X lido for diferente de zero. Para
cada valor de X apresente na tela se é par ou ímpar.'''
x = 1
while x != 0:
    x = int(input("Digite x: "))
    print(x, end = '  ')
    if x % 2 == 0:
        print("é par.")
    else:
        print("é impar")
    x = x + 1
else:
    print("x é zero")