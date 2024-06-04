pt = int(input("Digite o primeiro valor: "))
r = int(input("Digite a diferença entre os valores: "))
décimo = pt + (10 - 1) * r
for i in range(pt, décimo + r, r):
    print(i)