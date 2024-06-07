"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo."""
                                                                                                                                                                       
n = 0
v = 1
while True:
    n = int(input('Você quer ver a tabuada de qual valor? (Negativo parar parar) '))
    if n < 0:
        print('Saindo do programa...')
        break
    for v in range (1, 11):
        tab = n * v
        print(f'{n} x {v} = {tab}')
