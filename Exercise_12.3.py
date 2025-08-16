'''Altere o programa anterior mudando a regra de cálculo da média final. Na nova regra as notas de
prova P1, P2 e P3 devem ser analisadas e a menor nota deve ser descartada. As duas melhores notas
serão chamadas de N1 e N2. A nota de trabalho será considerada e a nova fórmula é:
MF = 0.4 * N1 + 0.4 * N2 + 0.2 * NT
(P1 P2 P3 NT): 5.0 5.0 5.0 10.0
N1 = 5.0; N2 = 5.0; NT = 10.0 -> Média = 6.9 Situação: REPROVADO
(P1 P2 P3 NT): 7.5 6.2 6.4 9.8
N1 = 6.4; N2 = 7.5; NT = 9.8 -> Média = 7.5 Situação: APROVADO
(P1 P2 P3 NT): 6.8 8.3 7.2 8.5
N1 = 7.2; N2 = 8.3; NT = 8.5 -> Média = 7.9 Situação: APROVADO'''

def CalculaMedia(pNotas):
    """Recebe o string pNotas, faz a separação dos valores, calcula e retorna a média"""
    pNotas = pNotas.split() # pNotas recebido também será usado como retorno da função
    for i in range(len(pNotas)): # converte as notas lidas para float
        pNotas[i] = float(pNotas[i])
    nota_descartada = min(pNotas)
    pNotas.remove(nota_descartada)
    media = pNotas[0] * 0.4 + pNotas[1] * 0.4 + pNotas[2] * 0.2
    situacao = 'APROVADO' if media >= 7 else 'REPROVADO'
    pNotas.append(media) # acrescenta media na lista de retorno
    pNotas.append(situacao) # acrescenta situacao na lista de retorno
    return pNotas

notas = input('Digite 4 notas (P1 P2 P3 NT): ')
resultado = CalculaMedia(notas) # chama a função que retorna a lista com resultados
print(f'N1 = {resultado[0]:.1f}; ', end='')
print(f'N2 = {resultado[1]:.1f}; ', end='')
print(f'NT = {resultado[2]:.1f} -> ', end='')
print(f'Média = {resultado[3]:.1f} '
, end='')
print(f'Situação: {resultado[4]}')