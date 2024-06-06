"""Crie um programa que vai ler vários números e colocar em uma lista


listaNum = []
c = 0
resp = 'S'
while True:
    valor = int(input("Digite um valor: "))
    listaNum.append(valor)
    c += 1
    resp = str(input("Deseja continuar? [S/N] "))
    if resp in 'Nn':

        print(f'Você digitou {c} valores!')
        listaNum.sort(reverse=True)
        print(f'A ordem decrescente deles é {listaNum}!')
        if 5 in listaNum:
            print('O valor 5 foi digitado na lista!')
        else:
            print('O valor 5 não foi digitado na lista!')
        break"""

listaNum = []
resp = ''

while resp != 'N':
    listaNum.append(int(input('Digite um valor: ')))
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
listaNum.sort(reverse=True)
if 5 in listaNum:
    print(f'O valor 5 está na lista e está na posição {listaNum.index(5)}!')
else:
    print('O valor 5 não está na lista!')
print(f'Você digitou {len(listaNum)} valores!\n'
      f'Os valores em ordem decrescente foram {listaNum}')
