'''Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios quaisquer. Exiba a lista na tela.
Em seguida verifique se existem e elimine valores que estiverem repetidos, deixando apenas uma
ocorrência de cada. A ordem relativa dos elementos na lista não deve ser alterada, com exceção às
consequências da eliminação dos repetidos. Exiba a nova lista sem repetidos e o seu tamanho.'''

from random import randint

qtde = int(input("Digite a quantidade: "))
lst = []

for i in range(qtde):
    lst.append(randint(1 , 100))
print(f"Lista gerada:\n {lst}")


lst_unica = list(set(lst))  # Remove duplicatas

print(f"Lista sem repetidos:\n{lst_unica}")