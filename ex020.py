import random

n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("Digite o nome do quarto aluno: ")
listaSorteio = [n1, n2, n3, n4]
sorteio = random.shuffle(listaSorteio)
print("A ordem de apresentação será 1° {}, 2° {}, 3° {} e 4° {}".format(listaSorteio[0], listaSorteio[1], listaSorteio[2], listaSorteio[3]))