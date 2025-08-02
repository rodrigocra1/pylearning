'''Escreva uma função que receba dois números inteiros A e B como parâmetros de entrada e retorne
True se A for divisível por B e False caso contrário. Escreva o programa principal para testar a função.'''

def divisivel(A, B):
    return True if A % B == 0 else False

#body

valorA = int(input('Digite A: '))
valorB = int(input("Digite B: "))

if divisivel(valorA, valorB):
    print("Numero é divisivel")
else:
    print("Não é divisivel.")