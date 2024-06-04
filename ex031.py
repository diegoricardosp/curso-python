dist = float(input('Digite a distância da sua viagem em KM: '))
if dist <= 200:
    v1 = dist * 0.50
    print("O valor da sua viagem será de R${:.2f}.".format(v1))
else:
    v2 = dist * 0.45
    print("O valor da sua viagem será de R${:.2f}.".format(v2))