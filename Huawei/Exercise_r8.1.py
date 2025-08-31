LL = int(input('Digite a linha de calçados:'))
match LL:
    case 16:
        print("Bebê")
    case 23:
        print("Infantil Feminino")
    case 25:
        print("infantil Masculino")
    case 29:
        print("Infantil esportivo")
    case 42:
        print("Masculino formal")
    case 43:
        print("Masculino Casual")
    case 49:
        print("Print esportivo")
    case 52:
        print("Femino formal salto baixo")
    case 53:
        print('Feminino formal salto alto')
    case 55:
        print('Feminino casual salto baixo')
    case 56:
        print('Feminino casual salto alto')
    case 59:
        print('Feminino esportivo')
    case _:
        print('Código fornecido é inválido')