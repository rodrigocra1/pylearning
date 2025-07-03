""" Escreva um programa que leia do teclado o código de um produto e seu preço unitário. O código é
um string e o preço é real. Acrescente o par código:preço em um dicionário. O laço termina quando
for fornecido um string vazio para o código. Ao final, exibir código e preço, um produto em cada linha.

Altere a solução do exercício resolvido 10.1 para fazer a iteração com o método .items"""

produtos = {}
print('Leitura dos dados')
cod = input(' Digite o código: ')

while cod != '':
    preco = float(input('  Digite um o preço:   '))
    produtos[cod] = preco
    cod = input(('   Digite o código: '))

print('Fim da leitura dos dados')
print("Preço dos Produtos")

for items in produtos.items():
    print(f'  produto {items[0]} custa R$ {items[1]: 7.2f}')