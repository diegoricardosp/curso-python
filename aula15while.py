num = s = 0
while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    s += num
'''print('A soma vale {}!'.format(s))'''
print(f'A soma vale {s}!')