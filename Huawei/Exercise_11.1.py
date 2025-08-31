'''Reescreva o programa exercício resolvido 11.6 usando um dicionário aninhado no lugar da tupla
como valor para o dicionário Estoque.'''

Estoque = {}
for linha in open('entrada_er_11.6.txt', 'r'):
    lst = linha.rstrip().split(';')
    print(lst)
    cod = int(lst[0])
    qtde = int(lst[1])
    pcunit = float(lst[2])
    valores = {'Codigo': cod, 'Quantidade': qtde, 'Unitario': pcunit}
    Estoque[cod] = valores

print("Valores carregados no dic:")
print(Estoque)

print("\nExibição dos dados na forma de tabela")
TotGeral = 0
for cod, dados in Estoque.items():
    TotGeral += dados['Quantidade'] * dados['Unitario']
    print(f'{cod}: {dados['Quantidade']:5d} x {dados['Unitario']:6.2f} = {dados['Quantidade'] * dados['Unitario']:8.2f}')
print(' ' * 24, f'{TotGeral:8.2f}')
