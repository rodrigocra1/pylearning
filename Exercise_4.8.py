'''Escreva um programa que leia um número inteiro que representa um ano. Informe se esse ano é
bissexto ou não.
Regra:
O ano é bissexto se cumprir uma das seguintes condições:
a) ser múltiplo de 4 e ao mesmo tempo não ser múltiplo de 100
b) ser múltiplo de 400'''

ano = int(input("Digite o ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano não é bissexto!")

