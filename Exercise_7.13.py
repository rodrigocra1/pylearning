'''Escreva um programa que permaneça em laço lendo três dados de um produto: o código (int), o
preço de compra (float) e o preço de venda(float). Com esses dados forme uma tupla e armazene-a
em uma lista. Os três dados devem ser lidos em uma única linha separados por espaço em branco.
O laço termina quando forem digitados três zeros: 0 0 0
Em seguida, para todas as tuplas presentes na lista, exiba o código do produto e a margem bruta de
lucro do produto em porcentagem e com uma casa decimal.
A margem bruta de lucro é calculada com a expressão:
𝑀𝑎𝑟𝑔𝑒𝑚𝐵𝑟𝑢𝑡𝑎 = ( 𝑃𝑟𝑒ç𝑜 𝑉𝑒𝑛𝑑𝑎
𝑃𝑟𝑒ç𝑜 𝑑𝑒 𝐶𝑜𝑚𝑝𝑡𝑎
− 1 ) . 100%'''

lst = []
while True:
    cod = int(input("Digite o codigo do produto: "))
    cprice = float(input("Digite o preço de compra: "))
    vprice = float(input("Digite o preço de venda: "))
    if cod == 0 and cprice == 0 and vprice == 0:
        break
    tupl = (cod, cprice, vprice)
    lst.append(tupl)

for i in lst:
    cod = i[0]
    cprice = i[1]
    vprice = i[2]
    bruts = ((vprice / cprice) - 1) * 100
    print(f"Código {cod}: {bruts:.1f}%")

