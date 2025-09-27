import random



def selectPouI():
    userSelection = int(input("Selecione: \n1 - Par\n2 - Impar\nSua escolha: "))
    while True:
        if userSelection == 1:
            return 'Par'
            break
        elif userSelection == 2:
            return 'Impar'
            break
        else:
            print("Digite uma opção válida")

def PCTurn():
    pcTurnNumber = int(random.randint(1,10))
    if pcTurnNumber %2 == 0:
        return 'Par'
    else:
        return 'Impar'

def UsrTURN():
    userTurnNumber = int(input("Digite um número de 1 a 10: "))
    if userTurnNumber %2 == 0:
        return 'Par'
    else:
        return 'Impar'


bet = selectPouI()
pcTurn = PCTurn()
userTUrn = UsrTURN()

print(bet)
print(pcTurn)
print(userTUrn)

