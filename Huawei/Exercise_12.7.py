'''Escreva uma função que carregue e retorne uma lista com todos os elementos da sequência de
Fibonacci menores que um parâmetro passado à função.
Escreva o programa principal para testar a função.
A sequência de Fibonacci é definida da seguinte forma: a) os dois primeiros termos da sequência
são 0 e 1. Do terceiro termo em diante cada termo é a soma dos dois anteriores.
Se ValorLimite = 120, então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89'''

def fibo(limit):
    a, b = 0, 1
    fiboSeq = []
    while a < limit:
        fiboSeq.append(a)
        a, b = b, a + b
    return fiboSeq

limit = int(input("Digite um limite: "))
fibo(limit)
fiboSeq = fibo(limit)
print(fiboSeq)
