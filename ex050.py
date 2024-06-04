r = 0
for i in range(0, 6):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        r += n
print("A soma dos números pares dos valores digitados é igual a {}!".format(r))