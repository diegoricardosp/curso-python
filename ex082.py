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