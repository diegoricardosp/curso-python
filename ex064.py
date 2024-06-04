num = 0
c = 0
soma = 0
num = int(input("Digite um número: "))
while num != 999:
    soma += num
    c += 1
    num = int(input("Digite um número: "))
print("Você digitou {} números e a soma é {}.".format(c, soma))