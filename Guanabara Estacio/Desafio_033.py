num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if (num1 > num2 and num1 > num3) and (num2 > num3):
    print(f"O maior número é o {num1}, o meno é o {num3}.")
elif (num2 > num1 and num2 > num3) and (num1 > num3):
    print(f"O maior número é o {num2}, o menor é o {num3}")
elif (num1 > num2 and num1 > num3) and (num3 > num2):
    print(f"O maior número é o {num1}, o menor é o {num2}.")
elif (num2 > num1 and num2 > num3) and (num1 < num3):
    print(f"O maior número é o {num2}, o menor é o {num1}")
elif (num3 > num1 and num3 > num2) and (num1 > num2):
    print(f"O maior número é o {num3}, o menor é o {num2}")
else:
    print(f"O maior número é o {num3}, o menor é o {num1}")