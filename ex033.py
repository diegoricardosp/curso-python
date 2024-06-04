n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 and n1 > n3:
    print('O número {} é maior que {} e {}'.format(n1, n2, n3))
elif n2 > n1 and n2 > n3:
    print('O número {} é maior que {} e {}'.format(n2, n1, n3))
else:
    print('O número {} é maior que {} e {}'.format(n3, n2, n1))