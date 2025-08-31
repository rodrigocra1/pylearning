'''Escreva um programa que leia dos inteiros A, B e carregue uma lista com todos os números primos
situados no intervalo fechado [A, B]. Use a função Primo() apresentada no exercício anterior. Ao
final exiba a lista na tela.
Adicionalmente escreva uma função para exibir a lista de primos de uma forma organizada na tela.'''

def Primo(V):
    '''Se V for primo retorna True, senão retorna False'''

    if V == 2:
        return True
    elif V % 2 == 0:
        return False
    else:
        raiz = pow(V, 0.5) # raiz quadradad e V
        i = 3
        while i <= raiz:
            if V % i == 0:
                return False
            i += 2
        return True
    
numA = int(input("Digite o primeiro número: "))
numB = int(input("Digite o segundo número: "))

listPrim = list()
listInt = list(range(numA, numB+1, 1))

for num in listInt:
    if Primo(num):
        listPrim.append(num)

print(listPrim)

