salario = float(input("Digite o seu salário: "))

if salario > 1250:
    aumento = salario * 1.1
    print(f"Com o aumento o seu salario é de R$ {aumento:.2f}.")
else:
    aumento = salario * 1.15
    print(f"Com o aumento o seu salario é de R$ {aumento:.2f}.")