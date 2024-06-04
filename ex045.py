from random import randint

print("---------- PEDRA/PAPEL/TESOURA ----------")
print("Você escolhe pedra, papel ou tesoura?")
opc = int(input("[1] Papel\n[2] Pedra\n[3] Tesoura\n"))
opc2 = randint(1,3)
print("Você escolheu {} e eu escolhi {}.".format(opc, opc2))
if opc == 1 and opc2 == 2:
    print("Você tirou papel e eu pedra, você ganhou!")
elif opc == 1 and opc2 == 3:
    print("Você tirou papel e eu tesoura, eu ganhei!!")
elif opc == 2 and opc2 == 1:
    print("Você tirou pedra e eu papel, eu ganhei!!")
elif opc == 2 and opc2 == 3:
    print("Você tirou pedra e eu tesoura, você ganhou!")
elif opc == 3 and opc2 == 1:
    print("Você tirou tesoura e eu tirei papel, você gamhou!")
elif opc == 3 and opc2 == 2:
    print("Você tirou tesoura e eu tirei pedra, eu ganhei!!")
else:
    print("Parece que escolhemos o mesmo item!")