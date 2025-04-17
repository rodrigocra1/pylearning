'''Leia um número inteiro entre 1 e 12 e exiba o mês correspondente. Caso seja digitado um número
fora desse intervalo, o programa deve exibir uma mensagem informando que não existe mês com
este número.'''

mes = int(input("Digite um numero correspondente a um mês: "))

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
cal = mes - 1

if mes >= 13 or mes <= 0:
    print("Entrada invalida")
else:
    print(meses[cal])