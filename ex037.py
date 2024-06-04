num1 = int(input("Digite um número: "))
opc = int(input("Você irá converter ele para: \n"
                "1 - Binário\n"
                "2 - Octal\n"
                "3 - Hexadecimal\n"))
if opc == 1:
    print("O número digitado é igual a {} na forma binária.".format(bin(num1)[2:]))
elif opc == 2:
    print("O número digitado é igual a {} na forma octal.".format((oct(num1)[2:])))
elif opc == 3:
    print("O número digitado é igual a {} na forma hexadecimal.".format(hex(num1)[2:]))
else:
    print("Opção inválida.")