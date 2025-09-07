from utilidades.moeda import moeda
from utilidades.dado import entrada


p = entrada.leiaDinheiro()
aumento = entrada.leiaInt('Digite a variação de aumento: ')
diminui = entrada.leiaInt('Digite a variação de redução: ')
moeda.resumo(p, aumento, diminui)