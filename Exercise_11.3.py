'''Escreva um programa que leia um número inteiro N (10 < N < 10.000) e grave um arquivo com N linhas
com os dados listados na tabela abaixo. O arquivo deve ter o nome 'Estoque.csv e deve usar o
caractere ';' (ponto e vírgula) como delimitador. Não é necessário que o arquivo esteja ordenado.
Campo Descrição
Código do produto Número inteiro entre 10000 e 50000. Gerar aleatórios. Não pode haver
repetição deste código e pede-se que não sejam sequenciais.
Quantidade em estoque Número inteiro entre 1 e 3800. Gerar aleatórios.
Preço unitário compra Número real entre 1.80 e 435.90. Gerar aleatórios.
Alíquota do ICMS Alíquota do imposto ICMS. Essa alíquota deve ser 7%, 12% ou 18%. (Não
colocar o caractere '%' no arquivo). Gerar aleatórios.
Dicas/sugestões (você pode segui-las ou não – é sua escolha)
- Para garantir que Código do Produto não tenha repetidos use um dicionário na geração dos dados.
- Gere os dados e coloque no dicionário. Depois grave no arquivo de saída.
- O valor dos elementos do dicionário pode ser no formato de tupla ou de dicionário aninhado.'''

from random import randint
