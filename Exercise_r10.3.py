'''Escreva um programa que leia dados dos Estados brasileiros: Sigla, Nome, Capital e PIB. A Sigla deve
ser usada como chave para o dicionário e o valor deve ser uma tupla formada com (Nome, Capital,
PIB). A leitura termina quando um string vazio for fornecido para a Sigla. Exibir os dados na tela.'''

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
    UF[sigla] = (estado, capital, pib)

print('\nDados dos Estados')
for items in UF.items():
    print(items)

print(' {:15} {:15} {:>10}'.format('Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in UF.items():
    print('({}) {:15} {:15} {:10.1f}'.format(
        sigla,
        dados[0],
        dados[1],
        dados[2] )
    )

print('Fim')