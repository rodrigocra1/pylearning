def leiaDinheiro():
    while True:
        try:
            preco = input( 'Digite o preco: R$ ')
            p = float(preco)
            return p
        except ValueError:
            print("Apenas números!")

def leiaInt(msg):
    while True:            
        try:
            valor = input(msg)
            aumento = int(valor)
            return aumento
        except ValueError:
            print("Apenas números!")