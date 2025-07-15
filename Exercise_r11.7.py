'''Neste exercício vamos verificar como funciona a codificação dos arquivos texto em Python.
Escreva um programa que grave as duas linhas de texto abaixo em um arquivo. Em seguida leia esse
arquivo e mostre na tela o que foi lido. As codificações que vamos testar são ANSI e UTF-8 e elas
deverão ser lidas do teclado.
Texto a ser gravado no arquivo
Gravação de Arquivo
acentos: á, é, í, Á, É, Í, ç, Ç'''

codGravacao = input('Digite a codificação de gravação:')
codLeitura = input('Digite a codificação de leitura:')

print('Etapa de gravacao')
arq = open('codificacao.txt', 'w', encoding=codGravacao)
arq.write('Gravação de Arquivo\n')
arq.write('acentos: á, é, í, Á, É, Í, ç, Ç\n')
arq.close()

print('\nEtapa de leitura do arquivo')
arq = open('codificacao.txt', 'r', encoding=codLeitura)
s = arq.readline()
print(s.rstrip())
s = arq.readline()
print(s.rstrip())
arq.close()
