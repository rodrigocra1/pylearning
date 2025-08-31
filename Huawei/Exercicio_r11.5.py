'''Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo
tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela. Mostrar
também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor. Usar
aqui o mesmo arquivo de entrada do exercício anterior.
Usar um iterador for e o arquivo como iterável.'''

Lst= []
for linha in open('entrada_r11.4.txt', 'r'):
    Lst.append(int(linha))

print('Lista do arquivo')
print(Lst)
Soma = sum(Lst)
print(f'Soma dos valores {Soma}')


print(f'Quantidade = {len(Lst)}')
print(f'Media dos valores = {sum(Lst)/len(Lst)}')
print(f"f'Minimo dos valores = {min(Lst)}")
print(f"Maximo do valores = {max(Lst)}")
