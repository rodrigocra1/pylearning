'''Crie uma função que receba um ângulo em graus, e retorne esse ângulo convertido para radianos. O
valor de PI está disponível no módulo math. Importe o módulo e use math.pi
Escreva o programa principal para testar a função.
AngRadiano = AngGraus * PI / 180'''

import math

def conGtoR(ang):
    AngGraus = ang
    AngRadiano = AngGraus * math.pi / 180
    print(f"O angulo {AngGraus} em Radianos é {AngRadiano}.")

ang = float(input("Digite o angulo em graus: "))
conGtoR(ang)
