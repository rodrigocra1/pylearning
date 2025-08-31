'''Altere a solução do ex.resolvido 7.3 incluindo o comando try-except na leitura dos números reais
para evitar a digitação incorreta dos valores. Quando ocorrer uma exceção uma mensagem deve ser
exibida na tela informando esta condição.
Relembre o tratamento de exceções consultando o capítulo 6, em especial o exemplo 6.4'''

try:
    N = int(input("Digite a qtde: "))
except ValueError:
    print("Digite um numero inteiro")
    exit()

L = []
for i in range(N):
    try:
        x = float(input(f"Elemento {i}: "))
        L.append(x)
        error = False
    except ValueError:
        print("Digite um numero real")
        error = True
        exit()

print("\nResultado")
for valor in L:
    print(f"  {valor:.2f}")
