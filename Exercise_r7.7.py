'''Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios. Exiba a lista na tela.
Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior
que zero. Para cada valor de X verifique se ele está ou não na lista gerada. Caso esteja é preciso exibir
a quantidade de ocorrências.'''

from random import randint
# primeira parte
lst = []
qtde = int(input("Digite a qtde: "))

for i in range(qtde):
    lst.append(randint(1, 20))
print(f"Lista gerada\n {lst}")

# segunda parte
X = 1
while X > 0:
     X = int(input("Digite X: "))
     if X in lst:
         print(f"   há {lst.count(X)} ocorrencias de {X} na lista")
     else:
         print(f"{X} não está na lista")
