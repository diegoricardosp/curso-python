""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

num = 0
c = 0
soma = 0
num = int(input("Digite um número: "))
while num != 999:
    soma += num
    c += 1
    num = int(input("Digite um número: "))
print("Você digitou {} números e a soma é {}.".format(c, soma))
