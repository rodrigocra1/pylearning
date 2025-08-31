'''No exercício resolvido 12.4 não foi feita uma validação do código lido do teclado. Sendo assim,
experimente digitar códigos que são menores que 10000 ou maiores que 99999 e veja o que
acontece.
Em seguida implemente a validação do código lido e só efetue o cálculo do dígito verificador se ele
for válido.'''

def CalcDigito(cod):
    s = str(cod)
    peso = 2
    dv = 0
    for a in s:
        dv += peso * int(a)
        peso += 1
    return dv % 7


codigo = int(input("Digite o código: "))
while codigo < 10000 or codigo > 99999:
    codigo = int(input("Digite o código entre 10000 e 99999: "))

while codigo > 0:
    digito = CalcDigito(codigo)
    print(f"Codigo: {codigo} -> digito: {digito}")
    cpdogp = int(input("Digite o codigo: "))