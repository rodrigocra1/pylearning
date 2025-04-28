'''Escreva um programa que permaneça em laço lendo quantidades (números inteiros) de produtos
vendidos. O laço termina quando for digitado zero ou um valor negativo. Ao término do laço exiba na
tela a soma de todas as quantidades digitadas (se for digitado um negativo para sair do laço ele não
deve afetar o total).'''

qnt = 1
total = 0
while qnt > 0:
    qnt = int(input("Digite a quantidade ou 0 para somar: "))
    total = total + qnt
else:
    print(f"Total: {total}")