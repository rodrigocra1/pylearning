'''Altere o programa do Exercício Proposto 7.8 acrescentando uma validação adicional para garantir
que a data fornecida seja válida. Por exemplo: a entrada 20242255 é válida segundo os critérios
estabelecidos no enunciado 7.8. Porém, 55/22/2024 não é uma data válida.
Neste exercício você deve garantir que a data seja válida (incluindo anos bissextos – para identificar
se um ano é bissexto veja o Exercício Proposto 4.8).'''

from curses.ascii import isdigit

data = input("Digite uma data no formato aaaammdd: ")
if len(data) != 8:
    print("Data está no formato errado.")
    exit()

elif not data.isdigit():
    print("Digite apenas numeros.")
    exit()

else:
    ano = int(data[:4])
    mes = int(data[4:6])
    dia = int(data[6:8])

if (mes < 1 or mes > 12) or (dia < 1 or dia > 31):
    print("Data invalida")
    exit()
elif (mes == 1 or mes == 3 or mes == 5  or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia < 1 or dia > 31):  # Janeiro, Março, Maio, Julho, Agosto, Outubro e Dezembro 31 dias
    print("Data invalida")
    exit()
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 1 or dia > 30):
    print("Data invalida")
    exit()
elif ano % 4 != 0:
        if mes == 2 and (dia < 1 or dia > 28):
            print("Data invalida")
            exit()
else:
    print(f"A data é: {dia}/{mes}/{ano}")

