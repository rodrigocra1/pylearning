'''Escreva um programa que leia um string contendo três números inteiros separados por espaços em
branco. Separe-os em objetos int, calcule sua soma e exiba na tela.
Entrada: 26 128 44 (string com três inteiros separados por espaço em branco)
Saída: n1 = 26
n2 = 128
n3 = 44
Soma = 198'''

valores = input("Digite 3 inteiros separados por espaço: ")
valores = valores.split()      # usa o método .split() para serparar os valores
for i in range(len(valores)):  # itera sobre a lista valores
    valores[i] = int(valores[i])   # e converte cada objeto para int
print(f"n1 = {valores[0]}")
print(f"n2 = {valores[1]}")
print(f"n3 = {valores[2]}")
print(f"Soma = {sum(valores)}")    # calcula e exibe a soma