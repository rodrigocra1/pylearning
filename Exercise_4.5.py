'''Escreva um programa que leia a idade de uma pessoa e indique qual sua classe eleitoral:
menor que 16 anos -> não eleitor
entre 18 completos e 65 anos incompletos -> eleitor obrigatório
entre 16 anos completos e 18 anos incompletos ou 65 anos completos -> eleitor facultativo'''

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não é eleitor!")
elif idade >= 16 and idade < 18 or idade >= 65:
    print("Eleitor facultativo")
else:
    print("Eleitor obrigatório")