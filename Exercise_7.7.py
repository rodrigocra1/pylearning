'''Altere a solução ex.resolvido 7.6 de modo que todos os valores repetidos rejeitados sejam incluídos
em uma segunda lista. Ao final exiba essa segunda lista juntamente com seu tamanho.'''

lstval = []
lstrejec = []
try:
    valor = int(input("Digite um inteiro: "))
    while valor != 0:
        if valor not in lstval:
            lstval.append(valor)
            valor = int(input("Digite um inteiro: "))
        else:
            lstrejec.append(valor)
            print(f"Erro, o valor {valor} ja está na lista.")
            valor = int(input("Digite um inteiro: "))
    print(f" a lista {lstval} contém {len(lstval)} elementos")
    print(f" a lista  de numeros rejeitados: {lstrejec} contém {len(lstrejec)} elementos")
except ValueError:
    print("VALOR INVALIDO")