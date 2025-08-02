'''No exercício resolvido 12.2 foi usado o comando condicional clássico. Altere o código dentro da
função substituindo o if-else clássico por um if de única linha.'''

def Paridade(a):
    return 'PAR' if a % 2 == 0 else 'IMPAR'
    

#body

n = int(input('Digite um numero inteiro: '))
print(Paridade(n))