'''Escreva um programa que leia três números inteiros: o primeiro termo P , a razão R e a quantidade Q
de termos de uma progressão aritmética. O programa deve calcular os Q termos da progressão
colocando-os em uma lista e no final exibi-la na tela.
obs: esse problema já foi abordado, sem o uso de listas, no exercício resolvido 5.3.'''



P = int(input("Digite o primeir termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Digite a quantidade da progressao: "))
a = 0
Termos = []
while a < Q:
    Termos.append(P)
    P = P + R
    a += 1
print("\nLista resultante")
print(Termos)
print("End")