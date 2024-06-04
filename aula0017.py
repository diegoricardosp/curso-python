"""num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o valor 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos!')"""

"""valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Acabou a lista!')"""

a = [2, 3, 4, 7]
b = a[:] #copia valores de lista
b[2] = 8
print(f'Lista A: {a}')
print(f'lista B: {b}')

