'''Nas eleições municipais os municípios com 200 mil eleitores ou mais tem segundo turno caso o
primeiro colocado não tenha mais do que 50% dos votos. Escreva um programa que leia o nome do
município, a quantidade de eleitores e a quantidade de votos do candidato mais votado e informe se
haverá segundo turno ou não.'''

mun = input("Digite o nome do municipio: ")
eleit = int(input("Digite o numero de eleitores: "))
if eleit < 200000:
    print(f"Não haverá segundo turno em {mun}")
    exit()
else:
    votos = int(input("Digite quantos votos obteve o candidato mais votado: "))


if votos > (eleit / 2):
    print(f"Não haverá segundo turno em {mun}")
    exit()
else:
    print(f"Haverá segundo turno em {mun}")
    exit()