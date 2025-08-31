'''Escreva um programa que leia um número inteiro e mostre na tela
 se ele é divisível por 10 ou não.
'''

n = int(input("Digite um número inteiro: "))

if n % 10 == 0:
    print("Número divisivel por 10!")
else:
    print("Número não divisivel por 10!")