''' Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com
três casas decimais. Usar o méthodo .writelines()'''

lst = []
X = float(input('Digite um numero real:  '))

while X != 0:
    lst.append(f"{X:.3f}\n")
    X = float(input('Digite um numero real:  '))

print(lst)
arq = open('saida_er_11.3.txt', 'w')
arq.writelines(lst)
arq.close()