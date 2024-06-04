pt = int(input("Digite o primeiro valor: "))
r = int(input("Digite a diferença entre os valores: "))
termo = pt
cont = 1
while cont <= 10:
    print(' {} >'.format(termo), end='')
    termo += r
    cont += 1
print("FIM!")
