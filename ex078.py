lista = []
for v in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {v}: ')))
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores: {lista}\n')
print(f'O maior número digitado foi {max(lista)} na posição {lista.index(max(lista))}!')
print(f'O menor número digitado foi {min(lista)} na posição {lista.index(min(lista))}!!')