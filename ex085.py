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