c = 0
num = 0
s = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        break
    c += 1
    s += num
print(f'Você digitou {c} números e as somas deles é igual a {s}.')