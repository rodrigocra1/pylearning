'''Escreva um programa que mostre na tela a tabuada do número inteiro N que deve ser lido do teclado.'''

N = int(input("Digite um numero inteiro: "))
tab = 0
cont = 1

while cont <= 10:
    tab = cont * N
    print(f"{N} x {cont} = {tab}")
    cont = cont + 1
print("Fim.")