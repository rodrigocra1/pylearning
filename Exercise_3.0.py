nome = input("Digite o nome do lutador: ")
Peso = float(input("Digite o peso do lutador: "))

if Peso < 52:
    Categoria = ''
elif Peso < 65:
    Categoria = 'Pena'
elif Peso < 72:
    Categoria = 'Leve'
elif Peso < 79:
    Categoria = 'Ligeiro'
elif Peso < 86:
    Categoria = 'Meio-médio'
elif Peso < 93:
    Categoria = 'Médio'
elif Peso < 100:
    Categoria = 'Meio-pesado'
else:
    Categoria = 'Pesado'

msg = f"O lutador {nome} pesa {Peso}, portanto é da categoria {Categoria}."

if Categoria == '':
    print(f'Peso inválido: {Peso}')
else:
    print(msg)
