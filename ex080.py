listaNum = []
numNovo = 0
for i in range(0,5):
    numNovo = int(input('Digite um valor: '))
    if i == 0 or numNovo > listaNum[-1]:
        listaNum.append(numNovo)
        print(f'Adicionei {numNovo} no final da lista, pois é o maior valor!')
    else:
        pos = 0
        while pos < len(listaNum):
            if numNovo <= listaNum[pos]:
                listaNum.insert(pos, numNovo)
                break
            pos += 1
        print(f'Adicionei {numNovo} na posição {listaNum.index(numNovo)}!')

print(f'Os valores digitados em ordem foram {listaNum}!')

