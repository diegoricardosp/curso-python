"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 
– Até 9 anos: MIRIM 
– Até 14 anos: INFANTIL 
– Até 19 anos: JÚNIOR 
– Até 25 anos: SÊNIOR 
– Acima de 25 anos: MASTER"""

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
