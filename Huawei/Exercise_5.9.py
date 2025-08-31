'''Escreva um programa que leia um número inteiro N. Em seguida calcule e mostre na tela o fatorial
de N (N!).'''


N = int(input("Digite um numero N: "))
fatorial = 1
contador = N

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {N} é {fatorial}")