'''Escreva um programa que leia 3 números inteiros e mostre na tela se eles formam um triângulo ou
não. Caso formem um triângulo informe o tipo de triângulo (equilátero, isósceles ou escaleno).
Para três números formarem um triângulo precisa ocorrer que:
os três números precisam ser maiores que zero;
a soma dos dois menores valores deve ser maior que o terceiro.'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 == 0 or n2 == 0 or n3 == 0:
    print("Medida invalida")
    exit()
elif n1 > n2 and n2 >=  n3:
    if (n2 + n3) < n1:
        print("Medida invalida")
elif n2 > n1 and n1 >= n3:
    if (n1 + n3) < n2:
        print("Medida invalida")
else:
    if n1 == n2 and n2 == n3:
        print("Triangulo equilatero")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("Tringulo isosceles")
    else:
        print("Triangulo escaleno")