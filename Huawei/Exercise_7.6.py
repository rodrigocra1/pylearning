'''Altere a solução ex.resolvido 7.4 para exibir as listas em ordem crescente'''

N = int(input("Digite um N: "))

lneg = []
lpos = []

for i in range(N):
    X = int(input(f"  elemento {i} >> "))
    if X >= 0:
        lpos.append(X)
    else:
        lneg.append(X)

lneg.sort()
lpos.sort()
print(f"\nLista de negativos {lneg}, contém {len(lneg)} elementos")
print(f"\nLista de positivos {lpos}, contém {len(lpos)} elementos")