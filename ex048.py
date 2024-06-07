"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s = s + i
        cont = cont + 1
print("Foram encontrados {} valores. A soma de todos os valores é de {}!".format(cont, s))
