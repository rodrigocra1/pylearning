distViagem = float(input("Digite a distãncia da viagem em km: "))

if distViagem <= 200:
    preco = distViagem * 0.5
    print(f"Sua viagem custa R$ {preco:.2f}.")
else:
    preco = distViagem * 0.45
    print(f"Sua viagem custa R$ {preco:.2f}.")