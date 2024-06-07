"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

tab = int(input("Digite o valor que deseja saber a tabuada: "))
for i in range(1, 11):
    result = tab * i
    print(tab, "x", i, "=", result)
