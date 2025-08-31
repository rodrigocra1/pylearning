'''Escreva um programa que leia um número inteiro N. Em seguida leia N números reais carregando-
os em uma lista. Ao final exiba os elementos da lista na tela, sendo um em cada linha'''

N = int(input("Digite a qtde: "))
L = []
for i in range(N):
    x = float(input(f"Elemento {i}: "))
    L.append(x)
print("\nResultado")
for valor in L:
    print(f"  {valor}")
