'''maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input("Digite o {}° peso: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}. O menor peso lido foi de {}.".format(maior, menor))'''

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')