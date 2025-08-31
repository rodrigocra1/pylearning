'''Em um determinado momento do dia a cotação de compra das moedas estrangeiras é a seguinte:
Dólar: US$ 1.00 = R$ 4.89 - Euro: € 1.00 = R$ 5.26 - Libra Esterlina: £ 1.00 = R$ 6.17
Escreva um programa que leia o tipo (D, E ou L maiúsculo) e o valor de moeda estrangeira que se
quer comprar e calcule o valor em reais necessários.'''

dol = 4.89
eur = 5.26
lib = 6.17

choice = input("Digite D para dolar; E para euro e L para libra: ")
if choice == 'D' or choice == 'E' or choice == 'L':
    quant = float(input("Digite a quantidade a ser comprada: "))
    if choice == 'D':
        result = dol * quant
        print(f"Valor em reais: {result}")
    elif choice == 'E':
        result = eur * quant
        print(f"Valor em reais: {result}")
    elif choice == 'L':
        result = lib * quant
        print(f"Valor em reais: {result}")
else:
    print("Entrada invalida")



