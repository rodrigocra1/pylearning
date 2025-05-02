'''Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios. Exiba a lista na tela.
Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior
que zero. Para cada valor de X verifique se ele está ou não na lista gerada. Caso esteja é preciso exibir
a quantidade de ocorrências.'''

from random import randint

lst = []
qtde = int(input("Digire a qtde: "))

for i in range(qtde):
    a = randint(1, 20)
    lst.append(a)
print(f"Lista gerada\n {lst}")