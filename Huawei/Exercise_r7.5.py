'''Escreva um programa que permaneça em laço lendo números inteiros. O laço termina quando for
digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado em uma lista. Ao final exiba
a lista na tela e a quantidade de elementos que ela contém.'''

lstval = []
valor = int(input("Digite um inteiro: "))
while valor != 0:
    lstval.append(valor)
    valor = int(input("Digite um inteiro: "))

print(f" a lista {lstval} contém {len(lstval)} elementos")