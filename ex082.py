"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

listaPar = []
listaImpar = []
listaTotal = []

while True:
    valor = int(input('Digite um valor: '))
    listaTotal.append(valor)
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if resp == 'N':
        print(f'A lista completa é {listaTotal}!')
        print(f'A lista de pares é {listaPar}!')
        print(f'A lista de impares é {listaImpar}!')
        break
