n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if media < 5:
    print("A sua média foi de {}. Você está reprovado.".format(media))
elif media >= 5 and media <= 6.9:
    print("A sua média foi de {}. Você está em recuperação.".format(media))
else:
    print("A sua média foi de {}. Você está aprovado!".format(media))