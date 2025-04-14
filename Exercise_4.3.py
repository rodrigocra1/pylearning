'''Uma empresa financeira concede empréstimos a pessoas físicas quando
o valor da parcela é menor que 8% do salário da pessoa. Escreva um programa
que leia dois números reais: o valor do salário e o valor da parcela e informe
se o empréstimo será concedido ou não.'''

sal = float(input("Digite o salário: "))
par = float(input("Digite o valor da parcela: "))


if par > sal * 0.08:
    print("O empréstimo não será concedido!")
else:
    print("O empréstimo será concedido!")