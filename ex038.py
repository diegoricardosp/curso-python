num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    print("O primeiro número ({}) é maior que o segundo número digitado ({}).".format(num1, num2))
elif num2 > num1:
    print("O segundo número ({}) é maior que o primeiro número digitado ({}).".format(num2, num1))
else:
    print("Os números são iguais!")