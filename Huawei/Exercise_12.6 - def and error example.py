'''Crie uma função que receba um número de 1 a 12 e retorne nome do mês correspondente. Se o valor
for outro o retorno da função deve ser o string "Inválido".
Escreva o programa principal para testar a função.'''


def toMonth(numMonth):
    monthName = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    print(monthName[numMonth])

def get_valind_month():
    while True:
        try:
            numInput = input("Digite o número do mês: ")
            num = int(numInput)

            # checa se o mes esta no range valido
            if num < 1 or num > 12:  
                print("Mês inválido!")
                continue

            return num # Retorna numero de mes valido
        
        except ValueError:
            print("Apenas números!")


numMonth = get_valind_month()
toMonth(numMonth)
