"""Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)."""

c = 0
num = 0
s = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        break
    c += 1
    s += num
print(f'Você digitou {c} números e as somas deles é igual a {s}.')
