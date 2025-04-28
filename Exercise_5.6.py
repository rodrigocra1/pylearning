'''Escreva um programa que permaneça em laço lendo cadeias de caracteres (strings). Para cada
cadeia digitada o programa deve exibir a cadeia seguida da quantidade de caracteres que ela
contém. O programa termina quando for digitado "FIM" (em letras maiúsculas).'''

string = ""

while True:
    if string != "FIM":
        string = input("Digite uma palavra ou digite FIM para sair: ")
        print(string, end='  ')
        print(len(string))
    else:
        print("Saindo")
        break