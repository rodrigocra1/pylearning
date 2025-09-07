def formatar(p):
    return f'R$ {p:.2f}'

def aumentar(p, n, formatar_result=False):
    res = p * (n/100) + p
    return formatar(res) if formatar_result else res

def diminuir(p, n, formatar_result=False):
    res = p - p * (n/100)
    return formatar(res) if formatar_result else res

def dobro(p, formatar_result=False):
    res = p * 2
    return formatar(res) if formatar_result else res

def metade(p, formatar_result=False):
    res = p / 2
    return formatar(res) if formatar_result else res

def resumo(p, aumento, diminui):
    print("-" * 40)
    print("RESUMO DO VALOR".center(40))
    print("-" * 40)
    print(f"{'Preço analisado:':<20}{formatar(p):>20}")
    print(f"{'Dobro do preço:':<20}{dobro(p, True):>20}")
    print(f"{'Metade do preço:':<20}{metade(p, True):>20}")
    print(f"{f'{aumento}% de aumento:':<20}{aumentar(p, aumento, True):>20}")
    print(f"{f'{diminui}% de redução:':<20}{diminuir(p, diminui, True):>20}")
