import random



def selectPouI():
    userSelection = int(input("Selecione: \n0 - Par\n1 - Impar\nSua escolha: "))
    while True:
        if userSelection == 0:
            return 0
            break
        elif userSelection == 1:
            return 1
            break
        else:
            print("Digite uma opção válida")
            userSelection = int(input("Selecione: \n0 - Par\n1 - Impar\nSua escolha: "))

    



'''Criar uma variavel gameResult com o gameSoma %2 '''
'''Criar o gameSoma antes do gameResult para usar no print fiinal'''

def gameLogic():
    gameSoma = pcTurnNumber + userTurnNumber ##verificar nomes das variaveis
    if bet == 0 and gameSoma %2 == 0: ##set userBet par = 0
        print(f"O computador escolheu {pcTurnNumber}, o resultado {gameSoma} é par!\nVocê ganhou!")
    elif bet == 1 and gameSoma %2 == 1:
        print(f"O computador escolheu {pcTurnNumber}, o resultado {gameSoma} é ímpar!\nVocê ganhou!")
    elif bet == 0 and gameSoma %2 == 1:
        print(f"O computador escolheu {pcTurnNumber}, o resultado {gameSoma} é ímpar!\nVocê perdeu!")
    elif bet == 1 and gameSoma %2 == 0:
        print(f"O computador escolheu {pcTurnNumber}, o resultado {gameSoma} é par!\nVocê perdeu!")



bet = selectPouI()
pcTurnNumber = int(random.randint(1,10))
userTurnNumber = int(input("Digite um número de 1 a 10: "))
while True:
    if userTurnNumber > 10:
        print("Digite uma opção válida")
        userTurnNumber = int(input("Digite um número de 1 a 10: "))
    else:
        break

gameLogic()