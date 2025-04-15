'''Escreva um programa para uma fábrica de calçados que leia o código LL de um calçado, que é um
número inteiro com 2 dígitos. Exiba na tela a linha do calçado, conforme a tabela a seguir. Se o
número fornecido não estiver na tabela, deve-se exibir a mensagem "Código inválido".
'''

ll = int(input("Digite o código LL: "))

if ll == 22:
    print("Bebê")
elif ll == 23:
    print("Infantil Feminino")
elif ll == 25:
    print("Infantil Masculino")
elif ll == 29:
    print("Infantil esportivo")
elif ll == 42:
    print("Masculino formal")
elif ll == 43:
    print("Masculino casual")
elif ll == 49:
    print("Masculino esportivo")
elif ll == 52:
    print("Feminino formal salto baixo")
elif ll == 53:
    print("Feminino formal salto alto")
elif ll == 55:
    print("Feminino casual salto baixo")
elif ll == 56:
    print("Feminino causal salto alto")
elif ll == 59:
    print("Feminino esportivo")
else:
    print("Código invalido!")