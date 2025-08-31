'''Escreva uma função que receba como parâmetro de entrada um número inteiro de 5 dígitos de
[10000, 99999] que represente códigos de produtos vendidos em uma loja. A função deve calcular e
retornar o dígito verificador utilizando a regra de cálculo explicada a seguir. Escreva o programa
principal para testar a função.
Considere o código 31483, em que cada dígito é multiplicado por um peso começando em 2 e
terminando em 6. Os valores obtidos são somados, e do total obtido calcula-se o resto de sua
divisão por 7.'''

def CalcDigito(cod):
    s = str(cod)
    peso = 2
    dv = 0
    for a in s:
        dv += peso * int(a)
        peso += 1
    return dv % 7

codigo = int(input("Digite o códgo: "))
while codigo > 0:
    digito = CalcDigito(codigo)
    print(f"Codigo: {codigo} -> digito: {digito}")
    cpdogp = int(input("Digite o codigo: "))