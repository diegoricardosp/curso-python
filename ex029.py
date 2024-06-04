limite = 80
velo = int(input('Digite a velocidade do carro: '))
calcMulta = velo - limite
multa = calcMulta * 7

if velo > limite:
    print("O veículo está acima da velocidade permitida. A multa será de R${:.2f}.".format(multa))
else:
    print("Parabéns por dirigir corretamente! O carro está no limite de velocidade.")