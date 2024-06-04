soma = 0
num = int(input("Digite um número: "))
resp = input("Deseja digitar mais um número? [S/N]")
while resp == 'S' or 's':
    soma =+ num
print("A soma dos valores é igual a {}.".format(soma))