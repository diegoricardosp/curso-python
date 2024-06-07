"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

pt = int(input("Digite o primeiro valor: "))
r = int(input("Digite a diferença entre os valores: "))
termo = pt
cont = 1
while cont <= 10:
    print(' {} >'.format(termo), end='')
    termo += r
    cont += 1
print("FIM!")
