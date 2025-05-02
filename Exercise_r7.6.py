'''Escreva um programa que permaneça em laço lendo números inteiros. O laço termina quando for
digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que
ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. Se um valor repetido for digitado,
o programa deve exibir uma mensagem na tela.
Ao final exiba a lista e a quantidade de elementos que ela contém.'''

lstval = []
valor = int(input("Digite um inteiro: "))
while valor != 0:
    if valor not in lstval:
        lstval.append(valor)
        valor = int(input("Digite um inteiro: "))
    else:
        print(f"Erro, o valor {valor} ja está na lista.")
        valor = int(input("Digite um inteiro: "))
print(f" a lista {lstval} contém {len(lstval)} elementos")