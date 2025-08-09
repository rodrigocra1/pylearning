'''Escreva uma função recursiva para calcular a somatória dos termos de uma Progressão Aritmética
definida pelos parâmetros Prim (primeiro termo), Razao e Qtde (quantidade de elementos). Esses
parâmetros devem ser lidos do teclado. Escreva o programa principal para testar a função, que deve
exibir na tela o valor dessa soma. Teste seu programa com os casos de teste a seguir.
Casos de teste: para Prim = 7; Razao = 4; Qtde = 7 → Soma = 133
para Prim = 12; Razao = 8; Qtde = 15 → Soma = 1020
para Prim = 2; Razao = 3; Qtde = 6 → Soma = 57'''

def soma(P, R, Q):
    if Q > 0:
        return P + soma(P+R, R, Q-1)
    else:
        return 0

Prim = int(input('Digite o primeiro termo: '))
Razao = int(input('Digite a razão: '))
Qtde = int(input('Digite a quantidade: '))
Resultado = soma(Prim, Razao, Qtde)
print(f'para Prim = {Prim}; Razao = {Razao}; Qtde = {Qtde} -> Soma = {Resultado}')