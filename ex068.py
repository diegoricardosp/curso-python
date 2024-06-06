"""Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randrange
v = 0
numjog = 0
numpc = 0
print('Jogo de par ou ímpar!')
while True:
    escjog = str(input("Par ou impar? [I/P] ")).upper().strip()[0]
    numjog = int(input('Digite um número: '))
    calc = numjog + numpc
    if escjog == 'P':
        numpc = randrange(1, 11, 2)
    elif escjog == 'I':
        numpc = randrange(0, 11, 2)
    calc = numjog + numpc
    if calc %2 == 0:
        if escjog == 'P':
            v += 1
        else:
            print(f'Você perdeu! Eu escolhi {numpc} e você escolheu {numjog}. A soma é {calc}, que é par.')
            print(f'Você ganhou {v} vezes consecutivas.')
            break
    elif calc %2 != 0:
        if escjog == 'I':
            v += 1
        else:
            print(f'Você perdeu! Eu escolhi {numpc} e você escolheu {numjog}. A soma é {calc}, que é ímpar.')
            print(f'Você ganhou {v} vezes consecutivas.')
            break
