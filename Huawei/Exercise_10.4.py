'''Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.
A chave deve o nome. O valor deve ser um dicionário aninhado contendo os demais dados. Se o
nome já existir no dicionário o programa deve perguntar se o usuário deseja alterar o cadastro.
Ao digitar um string vazio para o nome, o programa interrompe a leitura. Antes de encerrar o programa
apresente os dados em um formato de tabela.'''

contacts = {}
print('Iniciando contatos')

while True:
    name = input('Digite um nome: ')
    if name in contacts:
        print('\nNome já cadastrado!')
        YN = input(f'Deseja alterar o cadastro de {name}?\n Digite Y ou N: ').upper()
        match YN:
            case 'Y':
                phone = input('Digite o núnero de telefone: ')
                email = input('Digite o e-mail: ')
                birthday = input("Digite a data de aniversário: ")
                dictItem = {'phone':phone, 'email':email, 'birthday':birthday}
                contacts[name] = dictItem

            case 'N':
                print('Continuando o cadastro')
                continue

            case _:
                print('Opção inválida')
        continue
    elif name == '':
        print('Imprimindo lista...\n')
        break
    else:
        phone = input('Digite o núnero de telefone: ')
        email = input('Digite o e-mail: ')
        birthday = input("Digite a data de aniversário: ")
        dictItem = {'phone': phone, 'email': email, 'birthday': birthday}
        contacts[name] = dictItem

print('{:15} {:15} {:30} {:15}'.format('Nome', 'Tel.', 'E-mail', 'Aniversário'))
for name, dados in contacts.items():
     print('{:15} {:15} {:30} {:15}'.format(
        name,
        dados['phone'],
        dados['email'],
        dados['birthday'] )
     )
