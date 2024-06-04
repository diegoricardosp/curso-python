ano = int(input("Digite o seu ano de nascimento: "))
atual = 2023
idade = atual - ano
if idade <= 9:
    print("Você está na categoria Mirim!")
elif idade >= 10 and idade <= 14:
    print("Você está na categoria Infantil!")
elif idade >= 15 and idade <= 18:
    print("Você está na categoria Junior!")
elif idade >= 19 and idade <= 20:
    print("Você está na categoria Sênior!")
else:
    print("Você está na categoria Master!")