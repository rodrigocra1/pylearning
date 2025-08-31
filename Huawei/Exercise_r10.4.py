'''Escreva um programa que leia dados dos Estados brasileiros: Sigla, Nome, Capital e PIB. A Sigla deve
ser usada como chave para o dicionário e o valor deve ser um dicionário aninhado contendo os
objetos Nome, Capital e PIB. Um string vazio para a Sigla termina a leitura. Exibir os dados na tela.'''

UF = {}
print('Leitura dos dados')
while True:
    sigla = input("Digite a sigla do Estado:  ")
    if sigla == '':
        break
    elif sigla in UF:
        print(f'Sigla {sigla} já cadastrada')
        continue
    estado = input('Digite o nome do Estado: ')
    capital = input('Digite a capital: ')
    pib = float(input('Digite o PIB: '))
    dictItem = {'nome': estado, 'capital': capital, 'pib': pib}
    UF[sigla] = dictItem

print('\nDados dos Estados')
print(' {:15} {:15} {:>10}'.format('Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in UF.items():
    print('({}) {:15} {:15} {:10.1f}'.format(
        sigla,
        dados['nome'],
        dados['capital'],
        dados['pib'] )
    )

print('Fim')