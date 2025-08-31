'''Exemplo: Saída: Escreva um programa que leia um número inteiro nA e gere uma lista A com nA valores inteiros
aleatórios, não repetidos e situados na faixa [1, 100]. Mostre-a na tela em ordem crescente.
Em seguida leia outro inteiro nB e gere a lista B usando as mesmas regras aplicadas à lista A. Mostre-
a na tela também em ordem crescente.
Crie e exiba uma lista contendo a união das listas A e B, sem conter valores repetidos. Mostre a lista
resultante e a quantidade de elementos dela.
nA = 7 lista A = [8, 12, 29, 35, 44, 64, 81]
nB = 5 lista B = [10, 25, 35, 38, 64]
União de A e B
[8, 10, 12, 25, 29, 35, 38, 44, 64, 81] contém 10 elementos'''

from random import randint

nA = int(input("Digite a quantidade A: "))
A = []

for i in range(nA):
    A.append(randint(1 , 100))
    A.sort()
print(f"Lista gerada:\n {A}")

nB = int(input("Digite a quantidade B: "))
B = []

for i in range(nB):
    B.append(randint(1 , 100))
    B.sort()
print(f"Lista gerada:\n {B}")

C = list(set(A + B))
C.sort()

print(f"{C} contém {len(C)} elementos.")
