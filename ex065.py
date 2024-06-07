"""Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

soma = 0
num = int(input("Digite um número: "))
resp = input("Deseja digitar mais um número? [S/N]")
while resp == 'S' or 's':
    soma =+ num
print("A soma dos valores é igual a {}.".format(soma))
