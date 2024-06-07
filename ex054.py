"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date

hoje = date.today().year
maior = 0
menor = 0
for i in range(0,7):
    ano = int(input("Digite o ano do seu nascimento: "))
    niver = hoje - ano
    if niver >= 18:
        maior += 1
    else:
        menor += 1
print("Há {} pessoas maiores de 18 anos e {} menores que 18 anos!".format(maior, menor))
