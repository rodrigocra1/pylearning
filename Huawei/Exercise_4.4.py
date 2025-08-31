'''Escreva um programa que leia o nome de um aluno e as notas obtidas em três avaliações.
A média final é a média aritmética das três notas e a pessoa estará aprovada se
essa média for maior ou igual a 7.0. Mostre na tela o nome, a média
e a situação que será "Aprovado" ou "Reprovado".'''

aluno = input("Digite o nome do aluno: ")
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    status = "aprovado"
else:
    status = "reprovado"

print(f"O aluno {aluno} foi {status} com a media {media}.")
