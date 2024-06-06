"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

lista = []
for v in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {v}: ')))
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores: {lista}\n')
print(f'O maior número digitado foi {max(lista)} na posição {lista.index(max(lista))}!')
print(f'O menor número digitado foi {min(lista)} na posição {lista.index(min(lista))}!!')
