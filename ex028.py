import random

n1 = int(input('Digite um número de 0 até 5: '))
n2 = random.randint(0,5)
if n1 == n2:
    print('Parabéns! Você digitou o mesmo número que o computador pensou!')
else:
    print("O computador pensou no número {} e você no número {}.".format(n2, n1))