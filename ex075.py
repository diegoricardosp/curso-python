"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre: A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3. 
C) Quais foram os números pares."""

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o último valor: '))
listaNum = (n1, n2, n3, n4)
print(f'Você digitou os valores {listaNum}')
print(f'O número 9 foi digitado {listaNum.count(9)} vezes!')
if 3 in listaNum:
    print(f'O número 3 foi digitado no {listaNum.index(3)+1}° valor!')
else:
    print('O número 3 não foi digitado.')
print(f'Você digitou os números pares: ', end='')
for n in listaNum:
    if n % 2 == 0:
        print(n, end=' ')
