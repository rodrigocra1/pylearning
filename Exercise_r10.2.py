'''Escreva um programa que leia do teclado o código de um produto e seu preço unitário. O código é
um string e o preço é real. Acrescente o par código:preço em um dicionário. O programa deve
verificar se o código já está no dicionário e neste caso deve emitir uma mensagem de erro. O laço
termina quando for fornecido um string vazio para o código. Ao final, exibir código e preço, um
produto em cada linha.'''

produtos = {}
print('Leitura dos dados')

while True:
    cod = input(' Digite o código: ')
    if cod == '':
        break
    elif cod in produtos:
        print(f' Erro - codigo {cod} já existe')
        continue
    preco = float(input('  Digite um o preço:   '))
    produtos[cod] = preco


print('Fim da leitura dos dados')
print("Preço dos Produtos")

for cod in produtos.keys():
    print(f'  produto {cod} custa R$ {produtos[cod]: 7.2f}')