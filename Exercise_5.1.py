'''Reescreva o Exercício Resolvido 5.5 de modo a eliminar o comando if que foi acrescentado dentro
do laço while. Procure pensar em uma forma de eliminar esse condicional e ao mesmo tempo
manter o programa correto, totalizando e contando os valores diferentes de zero que forem
digitados.
Dica: a solução consiste em alterar a ordem dos comandos existentes dentro do laço while.'''

soma = qtde = 0
A = 1

while A != 0:
    A = int(input("Digite um numero inteiro: "))
    soma = soma + A
    qtde = qtde + 1
print(f"Soma dos valores = {soma}")
print(f"Quantidade: {qtde}")