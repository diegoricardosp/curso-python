peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))
imc = peso / (alt * alt)
print("Seu IMC é de {:.1f}.".format(imc))
if imc < 18.5:
    print("Você está abaixo do seu peso ideal!")
elif imc >= 18.5 and imc <= 25:
    print("Você está em seu peso ideal!")
elif imc > 25 and imc <= 30:
    print("Você está com sobrepeso!")
elif imc > 30 and imc <=40:
    print("Você está com obesidade!")
else:
    print("Cuidado, você está com obesidade mórbida.")
