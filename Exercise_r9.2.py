from PIL.MspImagePlugin import MspImageFile

Msg = "Digite Valor: "
print("Dados do primeiro conjunto")
C1 = set()  #primeiro conjunto vazio
x = int(input(Msg))
while x != 0:
    C1.add(x)  #acrescenta novo elemento, se ainda não estiver no conjunto
    x = int(input(Msg))
print("Dados do segundo conjunto")
C2 = set()
x = int(input(Msg))
while x != 0:
    C2.add(x) # acrescenta o novo elemento, se ainda não estiver no conjunto
    x = int(input(Msg))
print(f"\nConjunto 1: {C1}")
print(f"Conjunto 2: {C2}")
print(f"\nUnião de C1 e C2")
print (C1 | C2)
print("\nInterseção de C1 e C2")
print(C1 & C2)
print("\nFim do Programa")