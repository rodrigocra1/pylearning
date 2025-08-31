'''Escreva um programa que leia um número inteiro N. Em seguida leia N números inteiros carregando
os valores negativos em uma lista e os positivos em outra. Ao final exiba na tela cada uma das listas
juntamente como seu tamanho.
obs. Se o valor zero for fornecido ele deve ser incluído na lista de positivos.'''

N = int(input("Digite um N: "))

lneg = []
lpos = []

for i in range(N):
    X = int(input(f"  elemento {i} >> "))
    if X >= 0:
        lpos.append(X)
    else:
        lneg.append(X)

print(f"\nLista de negativos {lneg}, contém {len(lneg)} elementos")
print(f"\nLista de positivos {lpos}, contém {len(lpos)} elementos")