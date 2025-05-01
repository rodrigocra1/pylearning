'''Escreva um programa que leia um número inteiro e informe se esse número é primo ou não.
Lembrando: um número primo é divisível apenas por 1 e por ele mesmo.'''

N = int(input("Digite um N: "))
div = []
eh_primo = True
for i in range(2, N):  # 2 até N-1
    if N % i == 0:
        print("Não é primo")
        eh_primo = False
        break

if eh_primo:
    print("É primo")
