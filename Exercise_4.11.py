'''No comércio, o conceito de Margem Bruta é uma porcentagem que é aplicada ao preço de custo
para se obter o preço de venda. Uma loja tem como política comercial aplicar uma margem bruta de
45% quando o preço de custo de um produto é menor ou igual a R$ 100,00. Se o produto custa mais
que isso a margem bruta é de 35%. Escreva um programa que leia o preço de custo do produto e
mostre na tela qual o seu preço de venda, com duas casas decimais.'''

bruto = float(input("Digite o valor bruto: "))

if bruto <= 100.00:
    venda = bruto + bruto * 0.45
    print(f"Preço de venda: {venda}")
else:
    venda = bruto + bruto * 0.35
    print(f"Preço de venda: {venda}")