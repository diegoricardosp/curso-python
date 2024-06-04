listaNum = []
while True:
    numDigi = int(input("Digite um valor: "))
    if numDigi in listaNum:
        resp = str(input("Esse número já está na lista. Deseja continuar? [S/N] ")).upper().strip()[0]
        if resp in 'Nn':
            listaNum.sort()
            print(listaNum)
            break
        if resp in 'Ss':
            print('O valor não foi adicionado...')
    else:
        listaNum.append(numDigi)
        print("Número adicionado com sucesso...")
        resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
        if resp in 'Nn':
            listaNum.sort()
            print(f'Você digitou os valores {listaNum}!')
            break