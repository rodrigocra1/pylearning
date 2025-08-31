'''Escreva um programa que obrigatoriamente leia um inteiro que esteja no intervalo fechado
[100, 200]. Se o valor fornecido estiver fora do intervalo o programa deve avisar que o valor é inválido
e permanecer no laço. Quando um valor válido for fornecido o programa deve informar que o valor
foi aceito e terminar.'''

N = int(input("Digite N: "))

if N < 100 or N > 200:
    loop = False
else:
    print("Valor aceito")
    loop = True
i = 1
while loop == False:
    if N < 100 or N > 200:
        print("Entrada invalida")
        N = int(input("Digite N: "))
    else:
        print("Valor aceito")
        break
