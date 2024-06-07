"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

homVelho = 0
nomHomVelho = 0
contMulher = 0
medIdade = 0
somaIdade = 0
for i in range(0,4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = int(input("Digite seu sexo:\n[1] Masculino\n[2] Feminino\n"))
    somaIdade += idade
    medIdade = somaIdade / 4
    if i == 1 and sexo == 1:
        homVelho = idade
        nomHomVelho = nome
    if sexo == 1 and idade > homVelho:
        homVelho = idade
        nomHomVelho = nome
    if sexo == 2 and idade < 20:
        contMulher += 1
print("A média de idade do grupo é de {} anos. O homem mais velho é o {} e há {} mulhers menores de 20 anos.".format(medIdade, nomHomVelho, contMulher))
