'''Uma indústria metalúrgica adota um código de produto com o seguinte formato TMMM, onde T indica
o uso do produto, sendo 1 para residencial; 2 para industrial e MMM indica qual é o produto.
Escreva um programa que permaneça em laço até que seja digitado 0. Em cada repetição leia duas
informações:
a) O código do produto;
b) A quantidade vendida desse produto
O programa deve totalizar separadamente e exibir na tela as quantidades de produtos residenciais e
industriais vendidos. Se o dígito T do código não for 1 ou 2 deve ser mostrado "Tipo Inválido" e a
quantidade deve ser ignorada.'''

cod = 1
prod = 0
typeproduct = [0, 0]
while cod > 0:
    cod = int(input("Digite o codigo do tipo do produto: "))
    if cod != 1 and cod != 2:
        print("Codigo de produto invalido")
    elif cod == 1:
        typeproduct[0] += 1
        prod = input("Digite o codigo do produto: ")
    elif cod == 2:
        typeproduct[1] += 1
        prod = input("Digite o codigo do produto: ")
else:
    print(f"Total de produtos residenciais: {typeproduct[0]} ")
    print(f"Total de produtos industriais: {typeproduct[1]} ")