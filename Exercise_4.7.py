'''Em Albalândia mulheres e homens podem servir o exército do país. O serviço é opcional e é muito
comum que as pessoas se apresentem para o serviço em algum momento da vida. Existe uma única
restrição para ingresso que é a idade da pessoa: para mulheres a idade aceita é entre 21 e 34 anos;
para homens a idade aceita é entre 18 e 39 anos. Escreva um programa que leia três dados de
entrada: nome da pessoa, idade e sexo e informe se a pessoa será aceita ou não para o serviço.
Para o sexo deve ser lido apenas 1 caractere que pode ser 'f' ou 'F' para feminino e 'm' ou 'M'
para masculino, qualquer coisa diferente deve ser informado como inválido.'''

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo, F para feminino e M para masculino: ")
idade = int(input("Digite sua idade: "))

if sexo == "F" or sexo == "f":
    if idade > 21 and idade < 34:
        print(f"{nome} você foi aceita!")
    else:
        print(f"{nome} você não foi aceita!")
elif sexo == "M" or sexo == "m":
    if idade > 18 and idade < 39:
        print(f"{nome} você foi aceito!")
    else:
        print(f"{nome} você não foi aceito!")
else:
    print("Entrada inválida!")
    exit()