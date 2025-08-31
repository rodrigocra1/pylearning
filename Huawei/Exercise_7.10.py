'''Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios entre 1 e 100. Exiba a lista na tela.
Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior
que zero. Para cada valor de X verifique se ele está na lista gerada e caso esteja elimine-o. Se houver
mais de uma ocorrência de X na lista, elimine todas. Após as eliminações exiba a lista novamente.'''
from random import randint

qtde = int(input("Digite a quantidade: "))
lst = []

for i in range(qtde):
    lst.append(randint(1 , 100))
print(f"Lista gerada:\n {lst}")

X = 1
while X > 0:
    X = int(input("Digite um valor X: "))
    while X in lst:
        indice = lst.index(X)
        lst.pop(indice)
    print(lst)

