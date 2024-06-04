ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input("Digite um número de 0 até 20: "))
    if num not in range(0,19):
        num = int(input("Dados inválidos. Digite um número de 0 até 20: "))
    print(f'Você digitou o número {ext[num]}!')
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if resp == 'N':
        print("Fim do programa!")
        break
