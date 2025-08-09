'''Escreva um programa que verifique se um número inteiro lido é primo. Lembrando: um número
primo é divisível apenas por 1 e por ele mesmo. A verificação do primo deve ser feita dentro de uma
função.'''

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
    
N = int(input('Digite um inte: '))
if Primo(N):
    print(f'{N} é primo')
else:
    print(f'{N} não é primo')