"""from math import factorial
num = int(input("Digite o valor que precisa saber o fatorial: "))
f = factorial(num)
print("O fatorial de {} é igual {}.".format(num, f))"""

num = int(input("Digite o valor que precisa saber o fatorial: "))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))