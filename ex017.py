import math
lado = int(input("Digite um ângulo: "))
aco = math.acos(lado)
asi = math.asin(lado)
ata = math.atan(lado)
print("O cosseno do seu ângulo é {}, o seno é {} e a tangente é {}!".format(aco, asi, ata))