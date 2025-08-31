'''Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois.
Se ambos forem iguais, mostre qualquer um deles.'''

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 < n2:
    print(f"{n1} é o menor numero!")

else:
    print(f"{n2} é o menor número!")

print("\nSaindo...")