ano = int(input("Digite o seu ano de nascimento: "))
atual = 2023
idade = atual - ano
if idade < 18:
    print("Você irá se alistar em {} ano (s). Fique tranquilo :)".format(18 - idade))
elif idade == 18:
    print("Você precisa se alistar esse ano!!")
elif idade > 18:
    print("Você deveria ter se alistado há {} anos atrás.".format(idade - 18))