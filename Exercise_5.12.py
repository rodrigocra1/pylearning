'''Escreva um programa que leia dois inteiros: Qtde e Prim. Em seguida mostre na tela os Qtde termos
da sequência de Fibonacci que sejam maiores que Prim.'''

'''OK, FIQUEI FARTO DESSE EXERCICIO. O GPT FEZ'''


Qtde = int(input("Digite a quantidade de termos desejados: "))
Prim = int(input("Digite o valor mínimo (Prim): "))

fibo = [0, 1]
result = []

# Gera Fibonacci até encontrar Qtde números maiores que Prim
i = 2
while len(result) < Qtde:
    next_term = fibo[i - 1] + fibo[i - 2]
    fibo.append(next_term)

    if next_term > Prim:
        result.append(next_term)

    i += 1

print("Termos da sequência de Fibonacci maiores que", Prim, ":")
print(result)
