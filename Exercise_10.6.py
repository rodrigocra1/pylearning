'''Escreva um programa para registrar os seguintes dados de uma frota de veículos de uma empresa:
Placa (string – chave – obrigatório todas as letras maiúsculas)
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra (string no formato AAAAMMDD – ano,mês,dia)
O programa deve ficar em laço enquanto a Placa for digitada. O laço termina quando for digitado FIM
para a placa. Se for digitada uma placa com letras minúsculas o programa deve convertê-las para
maiúsculas com o método .upper().
Para cada veículo leia todos os dados e carregue em um dicionário. Se uma placa já existente for
digitada o programa deve avisar que já existe, mostrar seus dados e se usuário quiser fazer alteração
em algum dado basta digitar o novo valor. Para os campos em que nada for digitado deve ser mantido
o valor já cadastrado.
Ao final do laço mostre os dados na tela com uma formatação legível.
Desafio
Inclua no programa uma validação da placa, seguindo as seguintes regras:
a) Deve ter 7 caracteres
b) Os três primeiros devem ser letras
c) Os caracteres 4, 6 e 7 devem ser algarismos
d) O caractere 5 pode ser número (placa antiga) ou letra (nova placa padrão Mercosul)'''

frota = {}
print('Iniciando FROTAS')

while True:
    placa = input('Digite a placa: ').upper()
    if placa in frota:    #pergunta o que fazer em caso de placa já cadastrada
        print('\nPlaca já cadastrada!\n')

        print('{:15} {:15} {:15} {:15} {:15}'.format('Placa', 'Marca.', 'Modelo', 'Tipo', 'KM'))
        print('-' * 75)
        print('{:15} {:15} {:15} {:15} {:15}'.format(
            placa,
            frota[placa][0],
            frota[placa][1],
            frota[placa][2],
            frota[placa][3])
        )


        YN = input(f'\nDeseja alterar o cadastro de {placa}?\n Digite Y ou N: ').upper()
        match YN:
            case 'Y':
                edit = input(f'\nQual dado deseja editar:\n 1 - Marca\n 2 - Modelo\n 3 - Tipo\n 4 - KM\n Escolha uma opção: ')
                match edit:
                    case '1':
                        new_marca = input('Digite a marca do veículo: ')
                        print(f'Marca do veículo de placa {placa} foi editada.')
                        frota[placa] = (new_marca, frota[placa][1], frota[placa][2], frota[placa][3])
                    case '2':
                        new_modelo = input('Digite o modelo: ')
                        print(f'Modelo do veículo de placa {placa} foi editado.')
                        frota[placa] = (frota[placa][0], new_modelo, frota[placa][2], frota[placa][3])
                    case '3':
                        new_tipo = input("Digite o tipo do veículo: ")
                        print(f'Tipo do veículo de placa {placa} foi editado.')
                        frota[placa] = (frota[placa][0], frota[placa][1], new_tipo, frota[placa][3])
                    case '4':
                        new_km = input("Digite a kilometragem: ")
                        print(f'KM do veículo de placa {placa} foi editado.')
                        frota[placa] = (frota[placa][0], frota[placa][1], frota[placa][3], new_km)
                    case _:
                        print("Opção inválida")
                        continue

            case 'N':
                print('Continuando o cadastro')
                continue

            case _:
                print('Opção inválida')
        continue
    elif placa == 'FIM':
        print('Imprimindo lista...\n')
        break
    else:
        marca = input('Digite a marca do veículo: ')
        modelo = input('Digite o modelo: ')
        tipo = input("Digite o tipo do veículo: ")
        km = input("Digite a kilometragem: ")
        frota[placa] = ((marca, modelo, tipo, km))

print('{:15} {:15} {:15} {:15} {:15}'.format('Placa', 'Marca.', 'Modelo', 'Tipo', 'KM'))
print('-' * 75)

for placa, dados in frota.items():
        print('{:15} {:15} {:15} {:15} {:15}'.format(
            placa,
            dados[0],
            dados[1],
            dados[2],
            dados[3])
        )