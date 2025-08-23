'''Escreva uma função que receba uma lista como parâmetro de entrada e retorne uma tupla contendo
quatro valores na seguinte ordem: a soma, a média, o menor e o maior valor dentre todos os
elementos nela contidos. Considere que nessa lista ocorram apenas números reais. Escreva um
programa para testar essa função, exibindo na tela os resultados.'''

def valid_list():
    while True:
        try:
            lista = input("DIgite os numeros da lista :")
            lista = lista.split() # pNotas recebido também será usado como retorno da função
            for i in range(len(lista)):
                lista[i] = float(lista[i])
            return program(lista)
            
        except ValueError:
            print("Digite apenas numeros reais")

def program(lista):
    soma = sum(lista)
    media = soma / len(lista)
    maxim = max(lista)
    minim = min(lista)
    print(soma)
    print(media)
    resultado = (soma, media, maxim, minim)
    return resultado

resultado = valid_list()
print(resultado)