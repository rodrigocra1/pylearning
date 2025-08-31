'''Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.
A chave deve o nome. O valor pode ser uma tupla ou um dicionário aninhado. Você escolhe.
Ao digitar um string vazio para o nome, o programa interrompe a leitura e apresente todos dados na
tela na mesma formatação dos exercícios anteriores.
Neste exercício os nomes devem estar em ordem alfabética.
Dica
Use a função sorted() de Python.'''

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
                contacts[name] = ( (phone, email, birthday))

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
        contacts[name] = ( (phone, email, birthday))

sortedContacts = sorted(contacts.items())
print('{:15} {:15} {:30} {:15}'.format('Nome', 'Tel.', 'E-mail', 'Aniversário'))
print('-' * 75)

for name, dados in sortedContacts:
     print('{:15} {:15} {:30} {:15}'.format(
        name,
        dados[0],
        dados[1],
        dados[2] )
     )
