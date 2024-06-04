from random import randint

listaNum = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números sorteados foram {listaNum}.')
org = sorted(listaNum)
print(f'O menor número sorteado foi {org[0]} e o maior foi {org[4]}!')