'''Classificação indicativa é um conceito que se aplica à faixa etária para a qual uma obra
audiovisual se recomenda ou não. Suponha que um filme em cartaz no cinema tenha a Classificação de 16 anos.
Escreva um programa que leia a idade de uma pessoa e mostre se está de acordo ou não com a
classificação.'''

idade = int(input("Digite a idade: "))

if idade < 16:
    print("Esse filme não é indicado para essa idade!")
elif idade < 110:
    print("Esse filme pode ser assistido por essa pessoa.")
else:
    print("Essa pessoa ainda está viva?")