def calculoMulta(kmMedido):
    multa = (kmMedido - 80) * 7
    return multa

kmMedido = int(input("Digite a velocidade do carro: "))

if kmMedido > 80:
    print("Você estava acima da velocidade")
    multa = calculoMulta(kmMedido)
    print(f"Sua multa é de R$ {multa},00")
else:
    print("Você estava dentro do limite de velocidade!")
                    
