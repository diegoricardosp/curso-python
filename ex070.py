"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre: 
A) qual é o total gasto na compra. 
B) quantos produtos custam mais de R$1000. 
C) qual é o nome do produto mais barato."""

t = 0
m1000 = 0
vb = 0
b = ''
c = 0
while True:
    prod = str(input('Digite o nome do produto: '))
    v = float(input('Digite o valor do produto: R$'))
    t = t + v
    c += 1
    if v > 1000:
        m1000 += 1
    if c == 1:
        vb = v
        b = prod
    elif c != 1 and v < vb:
        vb = v
        b = prod
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        print(f'Você gastou R${t:.2f} na sua compra. Há {m1000} produtos acima de R$1000,00.\n'
              f'O produto mais barato é o produto {b} que custa R${vb:.2f}!')
        break
