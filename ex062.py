"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.""


pt = int(input("Digite o primeiro valor: "))
r = int(input("Digite a diferença entre os valores: "))
termo = pt
cont = 1
total = 0
resp = 10
while resp != 0:
    total = total + resp
    while cont <= total:
        print(' {} >'.format(termo), end='')
        termo += r
        cont += 1
    print(' Pausa!')
    resp = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos informados!".format(total))
