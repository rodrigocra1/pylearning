'''Escreva um programa que permaneça em laço enquanto um valor inteiro lido for diferente de zero.
Totalize e conte os valores digitados, exceto o zero, e apresente esses valores na tela. Totalizar é
somar os valores.'''

soma = qtde = 0
A = 1

while A != 0:
    A = int(input("Digite um numero inteiro: "))
    if A != 0:
        soma = soma + A
        qtde = qtde + 1
print(f"Soma dos valores = {soma}")
print(f"Quantidade: {qtde}")