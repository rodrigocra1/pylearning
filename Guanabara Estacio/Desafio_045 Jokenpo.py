import random

pcTurnNumber = int(random.randint(1,3))
if pcTurnNumber == 1:
    pcTurn = 'Pedra'
elif pcTurnNumber == 2:
    pcTurn = 'Papel'
else:
    pcTurn = 'Tesoura'


print(f'\n{" Jogo do Jokenpô ":=^30}\n')
userTurnNumber = int(input("Escolha uma opção:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n\nSua escolha: "))

while True:
    if userTurnNumber == 1:
        userTurn = 'Pedra'
        break
    elif userTurnNumber == 2:
        userTurn = 'Papel'
        break
    elif userTurnNumber == 3:
        userTurn = 'Tesoura'
        break
    else:
        print("Entrada inválida!")
        userTurnNumber = int(input("Sua escolha: "))

print(f"Você escolheu {userTurn}.\n")

if pcTurnNumber == 1 and userTurnNumber == 2:
    print(f"Computador: {pcTurn} x User: {userTurn}")
    print(f'\n{" Você ganhou! ":=^40}\n')
elif pcTurnNumber == 2 and userTurnNumber == 3:
    print(f"Computador: {pcTurn} x User: {userTurn}")
    print(f'\n{" Você ganhou! ":=^40}\n')
elif pcTurnNumber == 3 and userTurnNumber == 1:
    print(f"Computador: {pcTurn} x User: {userTurn}")
    print(f'\n{" Você ganhou! ":=^40}\n')
elif pcTurnNumber == userTurnNumber:
    print(f"Computador: {pcTurn} x User: {userTurn}")
    print(f'\n{" EMPATE ":=^40}\n')
else:
    print(f"Computador: {pcTurn} x User: {userTurn}")
    print(f'\n{" Você Perdeu! ":=^40}\n')
