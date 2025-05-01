'''Escreva um programa que leia uma quantidade Qtde e mostre na tela os Qtde primeiros termos da
sequência de Fibonacci.
A sequência de Fibonacci é definida da seguinte forma: a) os dois primeiros termos da sequência
são 0 e 1. Do terceiro termo em diante cada termo é a soma dos dois anteriores.
Se Qtde = 9, então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21'''

qtde = int(input("Insira uma quantidade: "))
fibo = [0,1]
print(len(fibo))

for i in range(2, qtde):
    fibo.append(fibo[i - 1] + fibo[i - 2])

print(fibo)