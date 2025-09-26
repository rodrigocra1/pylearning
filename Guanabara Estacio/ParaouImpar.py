'''Criar uma variavel gameResult com o gameSoma %2 '''
'''Criar o gameSoma antes do gameResult para usar no print fiinal'''

gameSoma = usrNumber + pcNumber ##verificar nomes das variaveis
gameResult = gameSoma % 2

def gameLogic():
    if usrBet == 0 and gameResult == 0: ##set userBet par = 0
        print(f"{gameSoma} é par!\nVocê ganhou!")
    elif usrBet == 1 and gameResult == 1:
        print(f"{gameSoma} é ímpar!\nVocê ganhou!")
    elif usrBet == 0 and gameResult == 1:
        print(f"{gameSoma} é ímpar!\nVocê perdeu!")
    else:
        print(f"{gameSoma} é par!\nVocê perdeu!")

