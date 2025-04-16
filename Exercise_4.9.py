'''a) b) c) Escreva um programa que leia 3 números inteiros e mostre na tela uma das seguintes opções:
"Os três valores são iguais"
"Há dois valores iguais e um diferente"
"Os três valores são diferentes"'''

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 == n2 and n1 == n3:
    print("Os numeros sao iguais!")
elif n1 == n2 or n1 == n2 or n2 == n3:
    print("Há dois valores iguais e um diferente")
else:
    print("Os três valores são diferentes")