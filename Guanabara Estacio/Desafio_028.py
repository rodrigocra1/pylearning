import random

def gameFunction():
    numPC = random.randint(1,5)
    numUsr = int(input("Digite um número de 1 a 5: "))

    while numUsr != 0:
        if numPC == numUsr:
            print(f"Parabéns! O número era {numPC}, você acertou!\nDigite outro número ou 0 para sair!")
        else:
            print(f"Que pena! O número era {numPC}, você errou! \nDigite outro número ou 0 para sair!")
        numPC = random.randint(1,5)
        numUsr = int(input("Digite um número de 1 a 5: "))


gameFunction()