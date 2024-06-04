import random
n1 = input("Digite um nome: ")
n2 = input("Digite outro nome: ")
n3 = input("Digite mais um nome: ")
listaSorteio = [n1, n2, n3]
sorteio = random.choice(listaSorteio)
print("O premiado foi {}!".format(sorteio))


