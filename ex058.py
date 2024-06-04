from random import randrange
cont = 1
num = int(input("Tente adivinhar o número que pensei de 0 à 10: "))
pc = randrange(0,11)
while num != pc:
    num = int(input("O valor está incorreto, tente novamente: "))
    cont += 1
print("Você acertou! Eu pensei {} e você jogou {}! Foram necessárias {} tentativas para isso acontecer. ".format(pc, num, cont))
