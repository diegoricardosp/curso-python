"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente."""

v = 0
num = []
pares = []
impares = []

for i in range(0, 7):
    v = int(input('Digite um valor: '))
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
num.append(impares[:])
num.append(pares[:])
num[0].sort()
num[1].sort()
print(f'Você digitou os valores pares {num[1]}!')
print(f'Você digitou os valores impares {num[0]}!')
