'''Escreva uma função que recebe um número inteiro como parâmetro de entrada e retorna o texto
"PAR" ou "ÍMPAR" . Use-a em um programa principal'''

def Paridade(a):
    return 'PAR' if a % 2 == 0 else 'IMPAR'
    

#body

n = int(input('Digite um numero inteiro: '))
print(Paridade(n))