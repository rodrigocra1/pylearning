'''Altere a solução ex.resolvido 7.3 para exibir os resultados em ordem crescente
Aplique o método .sort() apresentado no quadro 7.2 e visto no vídeo do exemplo 7.10'''

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

L.sort()
print("\nResultado")
for valor in L:
    print(f"  {valor:.2f}")
