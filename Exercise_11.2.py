'''Escreva um programa que leia um arquivo CSV de entrada que tenha dois inteiros em
cada linha. O primeiro é um código de produto e o segundo é a quantidade vendida. O
programa deve totalizar quantos itens foram vendidos para cada produto.
Dica: use um dicionário tendo o código como chave e a quantidade como valor. Para
cada código lido do arquivo verifique se ele já existe no dicionário usando o operador
in. Se não existir, inclua; se existir some a quantidade existente com a nova quantidade
lida do arquivo.'''
from Crypto.Util.py3compat import tostr

sumVendas = {}
for vendas in open('entrada_e11.2.csv'):
    lst = vendas.rstrip().split(';')
    cod = int(lst[0])
    qtde = ()

    if cod not in sumVendas:
        qtde = int(lst[1])
        sumVendas[cod] = qtde


    else:
        qtde = int(lst[1])
        sumVendas[cod] += qtde

for cod, dados in sumVendas.items():
    print(f'O produto de código {cod} teve {dados} vendas.')
