v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))
opc = 0
while opc != 5:
    print("Digite o que deseja fazer:\n"
              "[1] Somar\n"
              "[2] Multiplicar\n"
              "[3] Qual é o maior valor? \n"
              "[4] Novos números\n"
              "[5] Sair\n")
    opc = int(input("Digite a opção desejada: "))
    if opc == 1:
        soma = v1 + v2
        print("A soma de {} + {} é igual a {}!".format(v1, v2, soma))
    elif opc == 2:
        mult = v1 * v2
        print("A multiplicação de {} * {} é igual a {}".format(v1, v2, mult))
    elif opc == 3:
        if v1 > v2:
            print("O número {} é maior que {}!".format(v1, v2))
        else:
            print("O número {} é maior que {}!".format(v2, v1))
    elif opc == 4:
        v1 = int(input("Digite o novo valor: "))
        v2 = int(input("Digite o outro novo valor: "))
    elif opc == 5:
        print("Finalizando...")
    else:
        print("Opção inválida, digite novamente.")
print("Você saiu do programa. Obrigado por utilizar!")