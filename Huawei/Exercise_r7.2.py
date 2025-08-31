'''Usando a classe range, escreva um programa que leia três números inteiros: o primeiro termo P , a
razão R e a quantidade Q de termos de uma progressão aritmética. O programa deve calcular os Q
termos da progressão colocando-os em uma lista e no final exibi-la na tela.
obs: é o mesmo enunciado do exercício resolvido anterior 7.1'''

P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Digite a qtde de termos: "))
ultimo = P + R * (Q-1)
Termos = list(range(P, ultimo+1, R)) # a classe range gera a PA
print('Lista gerada com range')
print(Termos)
print('Fim do Programa')