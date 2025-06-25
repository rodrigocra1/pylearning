from random import randint
Qte = int(input("Digite um número inteiro: "))
if Qte > 50 or Qte < 1:
    print("Digite um número entre 1 e 50.")
    Qte = int(input("Digite um número inteiro: "))
conjunto = set()
while len(conjunto) < Qte:
    conjunto.add(randint(1,50))
print(conjunto)
print("Fim")