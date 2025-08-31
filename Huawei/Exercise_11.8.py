'''Escreva um programa para ler o arquivo CSV gerado no exercício proposto 11.7 com os dados de
uma frota de veículos de uma empresa:
Placa (string - chave)
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra (string no formato AAAAMMDD – ano,mês,dia)
O programa deve ler o arquivo, carregar um dicionário e exibir os dados na tela com um layout legível.'''

dicFrota = {}
for frota in open('Frota.csv'):
    lst = frota.rstrip().split(';')
    placa = lst[0]
    marca = lst[1]
    modelo = lst[2]
    tipo = lst[3]
    km = lst[4]
    dicFrota[placa] = (placa, marca, modelo, tipo, km)

print('{:15} {:15} {:15} {:15} {:15}'.format('Placa', 'Marca.', 'Modelo', 'Tipo', 'KM'))
print('-' * 75)

for placa, dados in dicFrota.items():
    print('{:15} {:15} {:15} {:15} {:15}'.format(placa, dados[0], dados[1], dados[2], dados[3], dados[4]))



