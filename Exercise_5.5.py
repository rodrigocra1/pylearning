'''Escreva um programa que leia três números inteiros: LMin, LMax e D. Em seguida exiba na tela todos
os valores divisíveis por D que estão dentro do intervalo fechado [LMin, LMax].'''

LMin = int(input("Digite o menor numero: "))
LMax = int(input("Digite o maior numero: "))
D = int(input("Digite um divisor: "))

L = []
i = LMin
while i < LMax:
    if i % D == 0:
        L.append(i)
    i += 1;

print(L)
