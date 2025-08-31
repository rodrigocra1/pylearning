'''Escreva um programa que leia dois números inteiros: LMin e LMax. Em seguida exiba na tela todos
os valores dentro do intervalo fechado [LMin, LMax].'''

LMin = int(input("Digite o menor numero: "))
LMax = int(input("Digite o maior numero: "))

L = []
i = LMin
while i < LMax:
    L.append(i)
    i += 1;


print(L)