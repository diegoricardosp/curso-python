num = int(input("Digite um número inteiro: "))
for i in range(2, num):
    if num % i == 0:
        print("Esse número é um número primo!")
    else:
        print("Esse número não é um número primo!")