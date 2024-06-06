"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

tabelaPreco = ("Teclado", 50, "Mouse", 30, "Gabinete", 300)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for produto in range(0, len(tabelaPreco)):
    if produto % 2 == 0:
        print(f'{tabelaPreco[produto]:.<30}', end='')
    else:
        print(f'R${tabelaPreco[produto]:>7.2f}')
print('-'*40)
