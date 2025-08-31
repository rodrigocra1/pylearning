'''Escreva um programa que mostre na tela os 10 primeiros termos de uma progressão aritmética (PA)
com primeiro termo P e razão R. Os dois números P e R são inteiros e devem ser lidos do teclado.'''

P = int(input("Digite o primeir termo: "))
R = int(input("Digite a razão: "))

cont = 0
while cont < 10:
    print(P)
    P = P + R
    cont = cont + 1
print("End")